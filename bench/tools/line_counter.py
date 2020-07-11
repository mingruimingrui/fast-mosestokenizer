#!/usr/bin/env python3

import sys
from tqdm import tqdm


for line in tqdm(sys.stdin):
    sys.stdout.write(line)
