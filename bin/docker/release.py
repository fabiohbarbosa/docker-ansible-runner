class Release(object):
  image_name = "ansible-runner"
  def __init__(self, distro, base, tag, file):
    self.distro = distro
    self.base = base
    self.tag = tag
    self.file = file
