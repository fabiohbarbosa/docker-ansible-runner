#!/usr/bin/env python
import os
import shutil
import sys
import unittest
from mock import MagicMock

sys.path.append('../../')

from docker import DockerReleaseGenerator, Release

class TestDockerReleaseGenerator(unittest.TestCase):

  @classmethod
  def setUp(self):
    self.path_config = 'config/distros/'
    self.file_generator = DockerReleaseGenerator(self.path_config)
    self.file_generator._DockerReleaseGenerator__build_folder = '/tmp/ansible-runner/test/'
    self.build_folder = self.file_generator._DockerReleaseGenerator__build_folder

  # generate
  def test_trace_generate(self):
    releases = []
    self.file_generator._DockerReleaseGenerator__create_build_folder = MagicMock()
    self.file_generator._DockerReleaseGenerator__release_adapter = MagicMock(return_value=releases)
    self.file_generator._DockerReleaseGenerator__generate_docker_files = MagicMock(return_value=releases)

    self.assertEquals(self.file_generator.generate(), releases)

    self.assertTrue(self.file_generator._DockerReleaseGenerator__create_build_folder.called)
    self.assertTrue(self.file_generator._DockerReleaseGenerator__release_adapter.called)
    self.assertTrue(self.file_generator._DockerReleaseGenerator__generate_docker_files.called)

  # create_build_folder
  def test_create_build_folder(self):
    self.file_generator._DockerReleaseGenerator__create_build_folder()
    build_folder = self.file_generator._DockerReleaseGenerator__build_folder

    self.assertTrue(os.path.exists(build_folder))
    shutil.rmtree(build_folder)
    self.assertFalse(os.path.exists(build_folder))

  # release_adapter
  def test_release_adapter_adapt_one_distro(self):
    releases = self.file_generator._DockerReleaseGenerator__release_adapter()

    self.assertEqual(len(releases), 2)

    jessie = releases[0]
    self.assertEqual(jessie.distro, 'debian')
    self.assertEqual(jessie.base, 'debian:jessie-slim')
    self.assertEqual(jessie.tag, 'debian-jessie')
    self.assertEqual(jessie.base_file, jessie.path_config + jessie.distro + '/' + 'Dockerfile_correct')
    self.assertEqual(jessie.generated_file, self.build_folder + 'Dockerfile_' + jessie.tag)

    wheezy = releases[1]
    self.assertEqual(wheezy.distro, 'debian')
    self.assertEqual(wheezy.base, 'debian:wheezy-slim')
    self.assertEqual(wheezy.tag, 'debian-wheezy')
    self.assertEqual(wheezy.base_file, wheezy.path_config + jessie.distro + '/' + 'Dockerfile_correct')
    self.assertEqual(wheezy.generated_file, self.build_folder + 'Dockerfile_' + wheezy.tag)

  # generate docker file
  def test_generate_docker_file(self):
    releases = []
    r = Release('debian', 'debian:jessie-slim', 'debian-jessie', 'Dockerfile_correct', self.path_config, self.build_folder)
    releases.append(r)

    self.file_generator._DockerReleaseGenerator__create_build_folder()
    self.file_generator._DockerReleaseGenerator__generate_docker_files(releases)
    self.assertTrue(os.path.exists(r.generated_file))

    shutil.rmtree(self.build_folder)
    self.assertFalse(os.path.exists(self.build_folder))

if __name__ == '__main__':
  unittest.main()
