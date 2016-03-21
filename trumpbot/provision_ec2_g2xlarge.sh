#!/bin/bash

sudo apt-get update
sudo apt-get install -y build-essential git python-pip libfreetype6-dev libxft-dev libncurses-dev libopenblas-dev  gfortran python-matplotlib libblas-dev liblapack-dev libatlas-base-dev python-dev python-pydot linux-headers-generic linux-image-extra-virtual
sudo apt-get install libhdf5-dev
sudo pip install -U pip

# Install CUDA 7
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1410/x86_64/cuda-repo-ubuntu1410_7.0-28_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1410_7.0-28_amd64.deb
sudo apt-get update
sudo apt-get install -y cuda
echo -e "\nexport PATH=/usr/local/cuda/bin:$PATH\n\nexport LD_LIBRARY_PATH=/usr/local/cuda/lib64" >> .bashrc  
sudo reboot

# Test that CUDA is working
cuda-install-samples-7.0.sh ~/
cd NVIDIA\_CUDA-7.0\_Samples/1\_Utilities/deviceQuery  
make  
./deviceQuery

# Clone the repo and install requirements
cd ~
sudo apt-get install python-numpy python-scipy python-dev python-pip python-nose g++ libopenblas-dev git
sudo pip install Theano


# Setup theano config
echo -e "\n[global]\nfloatX=float32\ndevice=gpu\n[mode]=FAST_RUN\n\n[nvcc]\nfastmath=True\n\n[cuda]\nroot=/usr/local/cuda" >> ~/.theanorc  

# Set Environment variables
# export CUDA_ROOT=/usr/local/cuda-7.0
# export PATH=$PATH:$CUDA_ROOT/bin
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CUDA_ROOT/lib64
# export THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32
# For profiling only
# export CUDA_LAUNCH_BLOCKING=1

sudo apt-get install libhdf5-dev libhdf5-serial-dev
sudo pip install Cython
sudo pip install h5py
sudo pip install keras
sudo pip install jupyter
sudo pip install nltk

python "import nltk; nltk.download('punkt')"
