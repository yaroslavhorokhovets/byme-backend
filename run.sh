#!/bin/bash
export name_image=byme_api
export port=8080
echo "Build image"
docker build -t $name_image:latest .

echo "Find container run by name"
container_run=$(docker ps | grep $name_image | awk '{ print $1 }')

if [[ $container_run ]]; then
  docker stop $container_run
  docker rm $name_image
fi

echo "Run"
docker run -d --name $name_image -p $port:$port $name_image

echo "Image not tag"
docker rmi $(docker images -f "dangling=true" -q) --force
