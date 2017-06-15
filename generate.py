#!/usr/bin/env python
import os, yaml, shutil, sys

path='docker-images/'
build_folder='.tmp'

#--- functions
def create_docker_file( base, tag, file ):
  docker_file_base = 'assets/'+file
  build_file = build_folder+'/Dockerfile_'+tag

  with open(docker_file_base, 'rt') as fin:
    with open(build_file, 'wt') as fout:
      for line in fin:
        fout.write(line.replace('__image__', base))

  return build_file

def docker_build( tag, build_file ):
  image_name='fabiohbarbosa/ansible-runner'
  image_name_tag=image_name + ':' + tag
  exit_code = os.system('docker build -t ' + image_name_tag + ' -f ' + build_file + ' .')
  if (exit_code != 0):
    print 'Error to build image: ' +image_name_tag
    sys.exit(1)
  else:
    print '#############################################################################'
    print '#############################################################################'
    print 'Success to build image "' + image_name_tag +' "'
    print '#############################################################################'
    print '#############################################################################'
  return image_name_tag

def docker_push(image_name_tag):
  exit_code = os.system('docker push '+image_name_tag)
  if (exit_code != 0):
    print 'Error to push image: ' +image_name_tag
    sys.exit(1)
  else:
    print '#############################################################################'
    print '#############################################################################'
    print 'Success to push image "' + image_name_tag +' "'
    print '#############################################################################'
    print '#############################################################################'

def build(items):
  tags = []
  for release, values in items:
    build_file = create_docker_file(values['base'], values['tag'], values['file'])
    tags.append(docker_build(values['tag'], build_file))
  return tags

def push(tags):
  for tag in tags:
    docker_push(tag)

#--- starter
distros = os.listdir(path)

if not os.path.exists(build_folder):
  os.makedirs(build_folder)
else:
  shutil.rmtree(build_folder)
  os.makedirs(build_folder)

for distro in distros:
  distro_path = path+distro
  release_file = distro_path + '/releases.yml'

  stream = yaml.load(open(release_file, 'r'))

  push(build(stream.items()))
sys.exit(0)
