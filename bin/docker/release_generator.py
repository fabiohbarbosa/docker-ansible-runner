import os, shutil, yaml
from release import Release

class DockerReleaseGenerator(object):
  __build_folder = '/tmp/ansible-runner/'

  def __init__(self, path_config='docker/config/distros/'):
    self.__path_config = path_config

  def generate(self):
    self.__create_build_folder()
    releases = self.__release_adapter()
    return self.__generate_docker_files(releases)

  def __create_build_folder(self):
    if not os.path.exists(self.__build_folder):
      os.makedirs(self.__build_folder)
    else:
      shutil.rmtree(self.__build_folder)
      os.makedirs(self.__build_folder)

  def __release_adapter(self):
    distros = os.listdir(self.__path_config)

    releases = []
    for distro in distros:
      release_file = self.__path_config + distro + '/releases.yml'
      stream = yaml.load(open(release_file, 'r'))
      for release, values in stream.items():
        releases.append(Release(distro, values["base"], values["tag"], values["base_file"], self.__path_config, self.__build_folder))

    return releases

  def __generate_docker_files(self, releases):
    for r in releases:
      with open(r.base_file, 'rt') as fin:
        with open(r.generated_file, 'wt') as fout:
          for line in fin:
            fout.write(line.replace('__image__', r.base))

    return releases
