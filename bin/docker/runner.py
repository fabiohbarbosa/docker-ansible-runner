import os
class DockerRunner(object):
  def __init__(self, docker_file, image_name, tag):
    self.docker_file = docker_file
    self.image_name = image_name
    self.tag = tag
    self.is_builded = bool(False)

  def build(self):
    repository = self.__repository()
    exit_code = os.system('docker build -t ' + repository + ' -f ' + self.docker_file + ' .')
    if (exit_code != 0):
      raise Exception
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
