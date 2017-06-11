#!/bin/bash
docker_image=ubuntu:17.04
docker_test=Dockerfile_test
image_name=ansible-runner-test

cp -a assets/Dockerfile ${docker_test}
sed -i "s/__image__/${docker_image}/g" ${docker_test}

docker build -t ${image_name} -f ${docker_test} .
docker run -it --rm  ${image_name} ansible --version

rm -rf  ${docker_test}

