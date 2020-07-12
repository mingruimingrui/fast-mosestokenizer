
**fast-mosestokenizer** is a C++ implementation of the moses tokenizer
which is a favourite among the folks in NLP research.

The reason for using this package over the original perl implementation is
for the purpose of portability.
With the C++ source code, you can use this library basically in every language.

The C++ script was adapted from the mosesdecoder repository
[`contrib/c++tokenizer`](https://github.com/moses-smt/mosesdecoder/tree/master/contrib/c%2B%2Btokenizer).

- [Benchmark](#benchmark)
- [Installation](#installation)
- [Usage (Command-line tool)](#usage-command-line-tool)
- [Usage (Python)](#usage-python)

## Benchmark

**fast-mosestokenizer** is also fast.
On english, it is about 6x faster than `tokenizer.perl` and 15x faster than
`sacremoses`.

see [./bench/README.md](./bench/README.md) for more information.

## Installation

Python users using `linux` and `osx>=10.15` can install directly from PyPI.

```sh
pip install fast-mosestokenizer
```

See [./INSTALL.md](./INSTALL.md) for more information.

## Usage (Command-line tool)

```sh
# Piping is the standard way to configure input and output stream.
# mosestokenizer would apply tokenization to each line of the input stream.
mosestokenizer en < infile > outfile

# For a full list of options, refer to the help message.
mosestokenizer -h
```

## Usage (Python)

```py
# Usage patterns are mostly the same as sacremoses.
>>> from mosestokenizer import MosesTokenizer

>>> tokenizer = MosesTokenizer('en')
>>> tokenizer.tokenize("""
The English name of Singapore is an anglicisation of the native Malay name for
the country, Singapura, which was in turn derived from the Sanskrit word for
lion city (romanised: Siṃhapura; Brahmi: 𑀲𑀺𑀁𑀳𑀧𑀼𑀭; literally "lion city"; siṃha
means "lion", pura means "city" or "fortress").[8]
""")
[
  'The', 'English', 'name', 'of', 'Singapore', 'is', 'an', 'anglicisation',
  'of', 'the', 'native', 'Malay', 'name', 'for', 'the', 'country', ',',
  'Singapura', ',', 'which', 'was', 'in', 'turn', 'derived', 'from', 'the',
  'Sanskrit', 'word', 'for', 'lion', 'city', '(', 'romanised', ':',
  'Siṃhapura', ';', 'Brahmi', ':', '𑀲𑀺𑀁𑀳𑀧𑀼𑀭', ';', 'literally', '"', 'lion',
  'city', '"', ';', 'siṃha', 'means', '"', 'lion', '"', ',', 'pura', 'means',
  '"', 'city', '"', 'or', '"', 'fortress', '"', ')', '.', '[', '8', ']'
]
```
