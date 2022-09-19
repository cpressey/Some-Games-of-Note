#!/usr/bin/env python3

import json
import sys
from urllib.parse import quote

with open(sys.argv[1], 'r') as f:
    data = json.loads(f.read())

n = {}
for key, value in data.items():
    assert 'anchor' in value and 'filename' in value
    n[key] = {
        "url": "https://github.com/cpressey/Some-Games-of-Note/blob/master/article/{}#{}".format(quote(value['filename']), value['anchor'])
    }

sys.stdout.write(json.dumps(n, indent=4, sort_keys=True))
