class Release(object):
  def __init__(self, distro, base, tag, base_file, path_config, build_folder):
    self.image_name = "fabiohbarbosa/ansible-runner"
    self.distro = distro
    self.base = base
    self.tag = tag
    self.path_config = path_config
    self.base_file = path_config + distro + '/' + base_file
    self.generated_file = build_folder + 'Dockerfile_' + tag
    self.build_folder = build_folder

  def __repr__(self):
    return "\n{\n  distro: %s \n  base: %s \n  tag: %s \n  path_config: %s\n  base_file: %s\n  generated_file: %s\n}\n" % (self.distro, self.base, self.tag, self.path_config, self.base_file, self.generated_file)

  def __str__(self):
    return "\n{\n  distro: %s \n  base: %s \n  tag: %s \n  path_config: %s\n  base_file: %s\n  generated_file: %s\n}\n" % (self.distro, self.base, self.tag, self.path_config, self.base_file, self.generated_file)

