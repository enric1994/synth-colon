import torch
from torch.autograd import Variable
import os
import argparse
from datetime import datetime
from lib.HarDMSEG import HarDMSEG
from utils.dataloader import get_loader,test_dataset
from utils.utils import clip_gradient, adjust_lr, AvgMeter
import torch.nn.functional as F
import numpy as np
from torchstat import stat


def structure_loss(pred, mask):
    
    weit = 1 + 5*torch.abs(F.avg_pool2d(mask, kernel_size=31, stride=1, padding=15) - mask)
    wbce = F.binary_cross_entropy_with_logits(pred, mask, reduce='none')
    wbce = (weit*wbce).sum(dim=(2, 3)) / weit.sum(dim=(2, 3))

    pred = torch.sigmoid(pred)
    inter = ((pred * mask)*weit).sum(dim=(2, 3))
    union = ((pred + mask)*weit).sum(dim=(2, 3))
    wiou = 1 - (inter + 1)/(union - inter+1)
    
    return (wbce + wiou).mean()



def test(model, path):
    
    ##### put ur data_path of TestDataSet/Kvasir here #####
    data_path = path
    #####                                             #####
    
    model.eval()
    image_root = '{}/images/'.format(data_path)
    gt_root = '{}/masks/'.format(data_path)
    test_loader = test_dataset(image_root, gt_root, 352)
    b=0.0
    # 50 = CVC-300 test size!
    for i in range(50):
        image, gt, name = test_loader.load_data()
        gt = np.asarray(gt, np.float32)
        gt /= (gt.max() + 1e-8)
        image = image.cuda()
        
        res  = model(image)
        res = F.upsample(res, size=gt.shape, mode='bilinear', align_corners=False)
        res = res.sigmoid().data.cpu().numpy().squeeze()
        res = (res - res.min()) / (res.max() - res.min() + 1e-8)
        
        input = res
        target = np.array(gt)
        N = gt.shape
        smooth = 1
        input_flat = np.reshape(input,(-1))
        target_flat = np.reshape(target,(-1))
 
        intersection = (input_flat*target_flat)
        
        loss =  (2 * intersection.sum() + smooth) / (input.sum() + target.sum() + smooth)

        a =  '{:.4f}'.format(loss)
        a = float(a)
        b = b + a
        
    return b/100



def train(train_loader, model, optimizer, epoch, test_path):
    model.train()
    # ---- multi-scale training ----
    size_rates = [0.75, 1, 1.25]
    loss_record2, loss_record3, loss_record4, loss_record5 = AvgMeter(), AvgMeter(), AvgMeter(), AvgMeter()
    best = 0.0
    for i, pack in enumerate(train_loader, start=1):
        for rate in size_rates:
            optimizer.zero_grad()
            # ---- data prepare ----
            images, gts = pack
            images = Variable(images).cuda()
            gts = Variable(gts).cuda()
            # ---- rescale ----
            trainsize = int(round(opt.trainsize*rate/32)*32)
            if rate != 1:
                images = F.upsample(images, size=(trainsize, trainsize), mode='bilinear', align_corners=True)
                gts = F.upsample(gts, size=(trainsize, trainsize), mode='bilinear', align_corners=True)
            # ---- forward ----
            #lateral_map_5, lateral_map_4, lateral_map_3, lateral_map_2 = model(images)
            lateral_map_5 = model(images)
            # ---- loss function ----
            loss5 = structure_loss(lateral_map_5, gts)
            
            
            #loss = loss2 + 0.4*loss3 + 0.4*loss4 + 0.2*loss5    # TODO: try different weights for loss
            loss = loss5
            # ---- backward ----
            loss.backward()
            clip_gradient(optimizer, opt.clip)
            optimizer.step()
            # ---- recording loss ----
            if rate == 1:
                
                loss_record5.update(loss5.data, opt.batchsize)
        # ---- train visualization ----
        if i % 20 == 0 or i == total_step:
            print('{} Epoch [{:03d}/{:03d}], Step [{:04d}/{:04d}], '
                  ' lateral-5: {:0.4f}]'.
                  format(datetime.now(), epoch, opt.epoch, i, total_step,
                          loss_record5.show()))
    save_path = 'snapshots/{}/'.format(opt.train_save)
    os.makedirs(save_path, exist_ok=True)
    
    
    if (epoch+1) % 1 == 0:
        meandice = test(model,test_path)
        if meandice > best:
            best = meandice
            torch.save(model.state_dict(), save_path + 'HarD-MSEG-best.pth' )
            print('[Saving Snapshot:]', save_path + 'HarD-MSEG-best.pth',meandice)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--epoch', type=int,
                        default=100, help='epoch number')
    
    parser.add_argument('--lr', type=float,
                        default=1e-4, help='learning rate')
    
    parser.add_argument('--optimizer', type=str,
                        default='Adam', help='choosing optimizer Adam or SGD')
    
    parser.add_argument('--augmentation',
                        default=False, help='choose to do random flip rotation')
    
    parser.add_argument('--batchsize', type=int,
                        default=16, help='training batch size')
    
    parser.add_argument('--trainsize', type=int,
                        default=480, help='training dataset size')
    
    parser.add_argument('--clip', type=float,
                        default=0.5, help='gradient clipping margin')
    
    parser.add_argument('--decay_rate', type=float,
                        default=0.1, help='decay rate of learning rate')
    
    parser.add_argument('--decay_epoch', type=int,
                        default=50, help='every n epochs decay learning rate')
    
    parser.add_argument('--train_path', type=str,
                        default='/synth-polyp/polyp-data/TrainDataset', help='path to train dataset')
    
    parser.add_argument('--test_path', type=str,
                        default='/synth-polyp/polyp-data/TestDataset/Kvasir' , help='path to testing Kvasir dataset')
    
    parser.add_argument('--train_save', type=str,
                        default='HarD-MSEG-best')
    
    opt = parser.parse_args()

    # ---- build models ----
    # torch.cuda.set_device(0)  # set your gpu device
    model = HarDMSEG().cuda()

    # ---- flops and params ----
    # from utils.utils import CalParams
    # x = torch.randn(1, 3, 352, 352).cuda()
    # CalParams(lib, x)

    params = model.parameters()
    
    if opt.optimizer == 'Adam':
        optimizer = torch.optim.Adam(params, opt.lr)
    else:
        optimizer = torch.optim.SGD(params, opt.lr, weight_decay = 1e-4, momentum = 0.9)
        
    print(optimizer)
    image_root = '{}/images/'.format(opt.train_path)
    gt_root = '{}/masks/'.format(opt.train_path)

    train_loader = get_loader(image_root, gt_root, batchsize=opt.batchsize, trainsize=opt.trainsize, augmentation = opt.augmentation)
    total_step = len(train_loader)

    print("#"*20, "Start Training", "#"*20)

    for epoch in range(1, opt.epoch):
        adjust_lr(optimizer, opt.lr, epoch, 0.1, 200)
        train(train_loader, model, optimizer, epoch, opt.test_path)
