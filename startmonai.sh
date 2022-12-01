#!/bin/bash
docker run -p 8080:8000 --gpus all --rm -ti --ipc=host --net=host projectmonai/monailabel:latest bash
monailabel apps --download --name radiology --output apps
monailabel datasets --download --name Task09_Spleen --output datasets
monailabel start_server --app apps/radiology --studies datasets/Task09_Spleen/imagesTr --conf models deepedit
