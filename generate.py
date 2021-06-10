#!/usr/bin/env python3

import os
import json
from os.path import join
from shutil import copy2
from jinja2 import Template

local_dir = '.local'
config_filename = 'config.json'
resource_filename = '.resource'
template_filename = '.template'
out_dir = 'out'

local_config = {}
with open(join(local_dir, config_filename)) as json_file:
    local_config = json.load(json_file)

tm = Template("My name is {{ local_config.name }} and I am {{ local_config.age }}")
msg = tm.render(local_config=local_config)

print(msg)

## Copy all files from template and replace the variables
for root, dirs, files in os.walk("template"):
    os.makedirs(join(out_dir, root),exist_ok=True)
    print(root)
    for file in files:
        if file.endswith(template_filename):
            f = open(join(root,file), "r")
            Template(f.read()).stream(local_config=local_config).dump(join(out_dir, root, file[:-len(template_filename)]))
        elif file.endswith(resource_filename):
            f = open(join(root,file), "r")
            copy2(join(local_dir, f.read()), join(out_dir, root, file[:-len(resource_filename)]))
        else:
            copy2(join(root, file), join(out_dir, root, file))
        print(join(root, file))
