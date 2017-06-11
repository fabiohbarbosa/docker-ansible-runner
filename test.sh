#!/bin/bash
docker_image=ubuntu:17.04
docker_test=Dockerfile_test
image_name=ansible-runner-test

check_status() {
  if [[ $1 != 0 ]]; then
    echo
    echo $2
    rm -rf  ${docker_test}
    exit $1
  fi
}

cp -a assets/Dockerfile ${docker_test}
sed -i "s/__image__/${docker_image}/g" ${docker_test}

docker build -t ${image_name} -f ${docker_test} .
check_status $? "Error to build docker image"

docker run -it --rm  ${image_name} ansible --version
check_status $? "Error to run container"

rm -rf  ${docker_test}
