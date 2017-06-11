#!/usr/bin/env python
import os, yaml, shutil, sys

path='docker-images/'
build_folder='.tmp'

#--- functions
def create_docker_file( base, tag ):
  docker_base_file='assets/Dockerfile'
  build_file = build_folder+'/Dockerfile_'+tag

  with open(docker_base_file, 'rt') as fin:
    with open(build_file, 'wt') as fout:
      for line in fin:
        fout.write(line.replace('__image__', base))

  return build_file

def docker_build( tag, build_file ):
  image_name='ansible-runner'
  image_name_tag=image_name + ':' + tag
  exit_code = os.system('docker build -t ' + image_name_tag + ' -f ' + build_file + ' .')
  if (exit_code != 0):
    sys.exit(1)
  return image_name_tag

def docker_push(image_name_tag):
  print '#######################################'
  print '#######################################'
  print '#######################################'
  print '#######################################'
  print os.environ['docker_login']
  print '#######################################'
  print '#######################################'
  print '#######################################'
  print '#######################################'
  exit_code = os.system('docker push '+image_name_tag)
  if (exit_code != 0):
    sys.exit(1)

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

  for release, values in stream.items():
    build_file = create_docker_file(values['base'], values['tag'])
    image_name_tag = docker_build(values['tag'], build_file)
    docker_push(image_name_tag)
