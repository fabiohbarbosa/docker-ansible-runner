Ansible Docker Runner
===

[![Build Status](https://travis-ci.org/fabiohbarbosa/docker-ansible-runner.svg?branch=master)](https://travis-ci.org/fabiohbarbosa/docker-ansible-runner)

## Description
Used to test Ansible **playbooks** and **roles**.

## How to use
Map your ansible playbook or role folder into **/runner** and pass command to container.

### Examples
#### Command line
```sh
docker run -it --rm  -v `pwd`:/runner \
   fabiohbarbosa/ansible-runner:ubuntu-17.04-zesty \
   ansible-playbook -i inventory test.yml
```

#### Docker Compose
```yaml
version: '3'
services:
  ansible-runner:
    image: fabiohbarbosa/ansible-runner:ubuntu-17.04-zesty
    container_name: ansible-runner
    command: ansible-playbook -i inventory test.yml
    volumes:
      - ./:/runner
```
