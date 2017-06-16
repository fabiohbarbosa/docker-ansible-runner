#--- functions
import os, shutil, yaml
from release import Release

class DockerReleaseGenerator(object):
  __path = 'docker/config/docker_images/'
  __build_folder = '/tmp/ansible-runner/'

  def generate(self):
    self.__create_build_folder()
    return self.__release_adapter()

  def __create_build_folder(self):
    if not os.path.exists(self.__build_folder):
      os.makedirs(self.__build_folder)
    else:
      shutil.rmtree(self.__build_folder)
      os.makedirs(self.__build_folder)

  def __release_adapter(self):
    distros = os.listdir(self.__path)

    releases = []
    for distro in distros:
      release_file = self.__path + distro + '/releases.yml'
      stream = yaml.load(open(release_file, 'r'))
      for release, values in stream.items():
        releases.append(Release(distro, values["base"], values["tag"], values["file"]))

    return releases
