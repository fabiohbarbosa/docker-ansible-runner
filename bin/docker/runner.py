import os
class DockerRunner(object):
  def __init__(self, build_folder, docker_file, image_name, tag):
    self.build_folder = build_folder
    self.docker_file = docker_file
    self.image_name = image_name
    self.tag = tag
    self.is_builded = bool(False)

  def build(self):
    repository = self.__repository()
    exit_code = os.system('cd ' + self.build_folder + ' && docker build -t ' + repository + ' -f ' + self.docker_file + ' .')
    if (exit_code != 0):
      raise Exception('Error to build docker file for ' + self.docker_file)
    self.is_builded = bool(True)


  def push(self):
    if not self.is_builded:
      raise Exception('Build image before run push')

    repository = self.__repository()
    exit_code = os.system('docker push ' +repository)
    if (exit_code != 0):
      raise Exception('Error to push image')

  def __repository(self):
    return self.image_name + ':' + self.tag
