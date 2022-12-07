#!/bin/bash
#docker volume create code
#docker cp -R dataset /code
#cp -R utils /code
#cp requirements.txt /code
cd ..
docker run -d -p 8080:8000 -v MonaiPipelineSetup:/code --gpus all --rm -ti --ipc=host --net=host projectmonai/monailabel:latest bash -c '
mkdir custom_data
monailabel apps --download --name radiology --output apps

monailabel start_server --app apps/radiology --studies custom_data --conf models deepedit'
