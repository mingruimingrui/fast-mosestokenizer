#!/usr/bin/env python3

import sys
import argparse
from mosestokenizer import MosesTokenizer


parser = argparse.ArgumentParser()

parser.add_argument('-l', '--lang', type=str, default='en', help='Language')
parser.add_argument(
    '-a', '--aggressive-dash-splits', action='store_true',
    help='Aggressively split dashes'
)
parser.add_argument(
    '-x', '--no-escape-xml', action='store_true',
    help='Escape XML characters'
)

args = parser.parse_args()

tokenizer = MosesTokenizer(
    lang=args.lang,
    aggressive_dash_splits=args.aggressive_dash_splits,
    escape_xml=not args.no_escape_xml,
)

for line in sys.stdin:
    tokens = tokenizer.tokenize(line)
    # sys.stdout.write(tokenizer.detokenize(tokens) + '\n')
    sys.stdout.write(' '.join(tokens) + '\n')
