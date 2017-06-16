#!/usr/bin/env python
import unittest
import sys
import os
from mock import MagicMock
sys.path.append('../../')

from docker import DockerRunner

class TestDockerRunner(unittest.TestCase):
  build_folder = '/tmp/ansible-runner/test/'
  correct_file = 'config/docker_files/Dockerfile_correct'
  incorrect_file = 'config/docker_files/Dockerfile_incorrect'
  image_name = 'fabiohbarbosa/ansible-runner'
  tag = 'test'

  # build tests
  def test_build_correct_file(self):
    os.system = MagicMock(return_value=0)

    self.docker = DockerRunner(self.build_folder, self.correct_file, self.image_name, self.tag)
    self.docker.build()
    self.assertTrue(os.system.called)
    self.assertTrue(self.docker.is_builded)

  def test_not_build_incorrect_file(self):
    os.system = MagicMock(return_value=1)

    self.docker = DockerRunner(self.build_folder, self.incorrect_file, self.image_name, self.tag)
    self.assertRaises(Exception, self.docker.build)
    self.assertTrue(os.system.called)
    self.assertFalse(self.docker.is_builded)

  # push tests
  def test_not_push_when_image_did_not_build(self):
    self.docker = DockerRunner(self.build_folder, self.correct_file, self.image_name, self.tag)
    self.assertRaises(Exception, self.docker.push)
    self.assertTrue(os.system.called)

  def test_push_when_image_is_already_built(self):
    os.system = MagicMock(return_value=0)

    self.docker = DockerRunner(self.build_folder, self.correct_file, self.image_name, self.tag)
    self.docker.build()
    self.docker.push()
    self.assertTrue(os.system.called)

if __name__ == '__main__':
  unittest.main()
