# Select a base image:

FROM pytorch/pytorch:1.1.0-cuda10.0-cudnn7.5-runtime

RUN pip install thop imageio torchstat scipy

RUN apt update -y
RUN apt install -y software-properties-common
RUN apt-add-repository -y ppa:octave/stable
RUN apt update -y
RUN apt install -y octave liboctave-dev

# cd eval
# pkg install -forge image
# pkg load image
# main

