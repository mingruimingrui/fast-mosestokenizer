#!/usr/bin/env python3

import sys
import argparse
from sacremoses import MosesTokenizer


parser = argparse.ArgumentParser()

parser.add_argument('-l', '--lang', type=str, help='Language')
parser.add_argument(
    '-a', '--aggressive-dash-splits', action='store_true',
    help='Aggressively split dashes'
)
parser.add_argument(
    '-x', '--no-escape-xml', action='store_true',
    help='Escape XML characters'
)

args = parser.parse_args()
aggressive_dash_splits = args.aggressive_dash_splits
escape = not args.no_escape_xml


tokenizer = MosesTokenizer(lang=args.lang)

for line in sys.stdin:
    line = tokenizer.tokenize(
        line,
        aggressive_dash_splits=aggressive_dash_splits,
        escape=escape,
        return_str=True
    )
    sys.stdout.write(line + '\n')
