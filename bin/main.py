#!/usr/bin/env python
import os, sys, logging
from docker import DockerReleaseGenerator, DockerRunner

logger = logging.getLogger('main.py')
logger.setLevel(logging.INFO)

releases = DockerReleaseGenerator().generate()
for r in releases:
  runner = DockerRunner(r.build_folder, r.generated_file, r.image_name, r.tag)
  runner.build()
  logger.info('Image "%s:%s" builded', r.image_name, r.tag)

for r in releases:
  runner.push()
  logger.info('Image "%s:%s" pushed', r.image_name, r.tag)
