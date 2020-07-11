import os
from glob import glob
from ctypes import cdll
from typing import List

__all__ = ['MosesTokenizer']

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_TOKENIZER_LIB_DIR = os.path.join(_THIS_DIR, 'lib')
_REQUIRED_LIBS = [
    'glib-2.0',
    'stdc++',
    're2',
    'boost_atomic',
    'boost_system',
    'boost_date_time',
    'boost_chrono',
    'boost_thread',
    'boost_program_options',
    'mosestokenizer-dev',
]

# Set default TOKENIZER_SHARED_DIR if not set
os.environ['TOKENIZER_SHARED_DIR'] = os.environ.get(
    'TOKENIZER_SHARED_DIR',
    os.path.join(_THIS_DIR, 'share')
)

# Manually load cached dynamic libraries before loading mosestokenizer
for _lib in _REQUIRED_LIBS:
    _wildcard = os.path.join(_TOKENIZER_LIB_DIR, 'lib{}.so*').format(_lib)
    for _fp in glob(_wildcard):
        try:
            cdll.LoadLibrary(_fp)
        except OSError:
            # Random note: ubuntu-16.04 won't be able to import glib-2.0
            # but it's okay
            pass

try:
    from mosestokenizer.lib import _mosestokenizer
except ImportError as e:
    _msg = "Failed to import mosestokenizer c++ library\n" + \
        "Full error log: {}".format(e.__repr__())
    raise RuntimeError(_msg)


class MosesTokenizer(_mosestokenizer.MosesTokenizer):
    """Moses tokenizer with C++ backend."""

    def __init__(
        self,
        lang: str = 'en',
        aggressive_dash_splits: bool = False,
        escape_xml: bool = False,
        unescape_xml: bool = False,
        refined_punct_splits: bool = False,
        penn: bool = False,
    ):
        params = _mosestokenizer.MosesTokenizerParameters()

        # TODO: Validate and expose other parameters
        # The reason for not exposing all params is because some of them are
        # not being used or necessary in the first place.
        params.lang_iso = lang
        params.verbose_p
        params.detag_p = True
        params.alltag_p
        params.entities_p
        params.escape_p = escape_xml
        params.aggro_p = aggressive_dash_splits
        params.supersub_p
        params.url_p
        params.downcase_p
        params.normalize_p  # Dummy variable
        params.penn_p = penn
        params.words_p  # Appears to be cli only variable
        params.denumber_p  # Dummy variable
        params.narrow_latin_p
        params.narrow_kana_p
        params.refined_p = refined_punct_splits
        params.unescape_p = unescape_xml
        params.drop_bad_p
        params.split_p
        params.notokenization_p
        params.para_marks_p
        params.split_breaks_p

        params.nthreads = 1
        params.chunksize = 1

        super().__init__(params)

    def tokenize(self, text: str) -> List[str]:
        return super().tokenize(text)

    def detokenize(self, text: str) -> List[str]:
        return super().detokenize(text)

    def split(self, text: str) -> List[str]:
        return super().split(text, False)
