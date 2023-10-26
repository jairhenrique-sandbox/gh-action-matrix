import os
import json
import github_action_utils as gha_utils

process = []

for root, dirs, files in os.walk('.'):
    if 'versions.txt' in files and 'Dockerfile' in files:
            a = root.replace('./','')

            with open(os.path.join(root,'versions.txt')) as f:
                data = f.read()

            for i in data.splitlines():
                process.append(f'{a}#{i}')

gha_utils.set_output('matrix',json.dumps({'matrix': process}))