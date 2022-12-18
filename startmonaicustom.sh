#!/bin/bash
cd ..
docker run -p 8080:8000 --gpus all --rm -ti --ipc=host --net=host projectmonai/monailabel:latest bash -c '
mkdir datasets
cd datasets
curl https://storage.googleapis.com/heart_data/Task03_Liver.tar -o datasets/liver.tar
tar -xvf liver.tar
cd ..
monailabel apps --download --name radiology --output apps
monailabel start_server --app apps/radiology --studies datasets/Task03_Liver/imagesTr --conf models deepedit'
