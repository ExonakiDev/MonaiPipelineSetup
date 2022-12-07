#!/bin/bash
cd ..
docker run -p 8080:8000 --gpus all --rm -ti --ipc=host --net=host projectmonai/monailabel:latest bash -c '
mkdir custom_data
curl https://storage.googleapis.com/heart_data/Task03_Liver.tar -o custom_data/liver.tar
cd custom_data
tar -xvf liver.tar
monailabel apps --download --name radiology --output apps
monailabel start_server --app apps/radiology --studies custom_data --conf models deepedit'
