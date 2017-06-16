#!/usr/bin/env python
import os, sys
from docker import DockerReleaseGenerator, DockerRunner

releases = DockerReleaseGenerator().generate()
for r in releases:
  runner = DockerRunner(r.build_folder, r.generated_file, r.image_name, r.tag)
  runner.build()

for r in releases:
  runner.push()
