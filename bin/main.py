#!/usr/bin/env python
import os, sys, logging
from docker import DockerReleaseGenerator, DockerRunner

releases = DockerReleaseGenerator().generate()
for r in releases:
  runner = DockerRunner(r.build_folder, r.generated_file, r.image_name, r.tag)
  runner.build()
  logging.info('Image '%s:%s' builded', r.image_name, r.tag)

for r in releases:
  runner.push()
  logging.info('Image '%s:%s' pushed', r.image_name, r.tag)
