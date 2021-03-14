#!/usr/bin/env python3
from jinja2 import Template
import yaml
import sys

template_name = sys.argv[1]
images = yaml.safe_load(open("codeship-meta.yml", "r").read())
steps = Template(open(template_name, "r").read(), trim_blocks=True)
print(steps.render(images=images))
