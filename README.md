
**fast-mosestokenizer** is a c++ implementation of the moses tokenizer
which is a favourite among the folks in NLP research.
I did not write the c++ script, it was taken directly from the mosesdecoder
repository [`contrib/c++tokenizer`](https://github.com/moses-smt/mosesdecoder/tree/master/contrib/c%2B%2Btokenizer)

- [Usage (Command-line tool)](#usage-command-line-tool)
- [Usage (Python)](#usage-python)

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
