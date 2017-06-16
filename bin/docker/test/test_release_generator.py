#!/usr/bin/env python
import os
import shutil
import sys
import unittest
from mock import MagicMock

sys.path.append('../../')

from docker import DockerReleaseGenerator

class TestDockerReleaseGenerator(unittest.TestCase):

  @classmethod
  def setUp(self):
    self.file_generator = DockerReleaseGenerator()

  # generate
  def test_trace_generate(self):
    releases = []
    self.file_generator._DockerReleaseGenerator__create_build_folder = MagicMock()
    self.file_generator._DockerReleaseGenerator__release_adapter = MagicMock(return_value=releases)

    self.assertEquals(self.file_generator.generate(), releases)

    self.assertTrue(self.file_generator._DockerReleaseGenerator__create_build_folder.called)
    self.assertTrue(self.file_generator._DockerReleaseGenerator__release_adapter.called)

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
    self.assertEqual(jessie.file, 'Dockerfile_correct')

    wheezy = releases[1]
    self.assertEqual(wheezy.distro, 'debian')
    self.assertEqual(wheezy.base, 'debian:wheezy-slim')
    self.assertEqual(wheezy.tag, 'debian-wheezy')
    self.assertEqual(wheezy.file, 'Dockerfile_correct')

if __name__ == '__main__':
  unittest.main()
