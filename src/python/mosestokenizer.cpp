#include <string>
#include <vector>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "mosestokenizer/Parameters.h"
#include "mosestokenizer/Tokenizer.h"

namespace py = pybind11;

#ifdef TOKENIZER_NAMESPACE
using namespace TOKENIZER_NAMESPACE ;
#endif


PYBIND11_MODULE(_mosestokenizer, m) {
    m.doc() = R"pbdoc(
        Pybind11 mosestokenizer plugin
        ------------------------------
        .. currentmodule:: _mosestokenizer
        .. autoclass:: MosesTokenizerParameters
        .. autoclass:: MosesTokenizer
    )pbdoc";

    py::class_<Parameters>(m, "MosesTokenizerParameters")
        .def(py::init<>())
        .def_readwrite("lang_iso", &Parameters::lang_iso)
        .def_readwrite("nthreads", &Parameters::nthreads)
        .def_readwrite("chunksize", &Parameters::chunksize)
        .def_readwrite("verbose_p", &Parameters::verbose_p)
        .def_readwrite("detag_p", &Parameters::detag_p)
        .def_readwrite("alltag_p", &Parameters::alltag_p)
        .def_readwrite("entities_p", &Parameters::entities_p)
        .def_readwrite("escape_p", &Parameters::escape_p)
        .def_readwrite("aggro_p", &Parameters::aggro_p)
        .def_readwrite("other_letters_p", &Parameters::other_letters_p)
        .def_readwrite("supersub_p", &Parameters::supersub_p)
        .def_readwrite("url_p", &Parameters::url_p)
        .def_readwrite("downcase_p", &Parameters::downcase_p)
        .def_readwrite("normalize_p", &Parameters::normalize_p)
        .def_readwrite("penn_p", &Parameters::penn_p)
        .def_readwrite("words_p", &Parameters::words_p)
        .def_readwrite("denumber_p", &Parameters::denumber_p)
        .def_readwrite("narrow_latin_p", &Parameters::narrow_latin_p)
        .def_readwrite("narrow_kana_p", &Parameters::narrow_kana_p)
        .def_readwrite("refined_p", &Parameters::refined_p)
        .def_readwrite("unescape_p", &Parameters::unescape_p)
        .def_readwrite("drop_bad_p", &Parameters::drop_bad_p)
        .def_readwrite("split_p", &Parameters::split_p)
        .def_readwrite("notokenization_p", &Parameters::notokenization_p)
        .def_readwrite("para_marks_p", &Parameters::para_marks_p)
        .def_readwrite("split_breaks_p", &Parameters::split_breaks_p);

    py::class_<Tokenizer>(m, "MosesTokenizer")
        .def(py::init<const Parameters&>())
        .def("init", &Tokenizer::init, "Reinitialize tokenizer shared dir.")
        .def("tokenize", &Tokenizer::tokens, "Tokenize sentence.")
        .def(
            "detokenize",
            (std::string (Tokenizer::*)(
                const std::vector<std::string>&
            )) &Tokenizer::detokenize,
            "Detokenize into sentence."
        )
        .def(
            "split",
            (std::vector<std::string> (Tokenizer::*)(
                const std::string &,
                bool *continuation_p
            )) &Tokenizer::splitter,
            "Split a paragraph into multiple sentences."
        );

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}
