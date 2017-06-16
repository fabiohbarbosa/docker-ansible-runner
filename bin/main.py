#!/usr/bin/env python
import os
from docker import DockerReleaseGenerator, DockerRunner

# print os.path.realpath('./')
# print os.path.normpath('.')

releases = DockerReleaseGenerator().generate()
print releases
