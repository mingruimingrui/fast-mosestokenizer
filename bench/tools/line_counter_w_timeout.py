#!/usr/bin/env python3

import sys
import argparse
from time import time
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--timeout', type=int, help='Timeout')
args = parser.parse_args()


start_time = time()
for line in tqdm(sys.stdin):
    if args.timeout and time() - start_time > args.timeout:
        break
    sys.stdout.write(line)
