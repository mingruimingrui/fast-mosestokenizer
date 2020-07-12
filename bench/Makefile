LANG=en
DATA_DIR=data
TOOLS_DIR=tools
OUTPUT_DIR=out

N=100000
TIMEOUT=15

IWSLT_ROOT=${DATA_DIR}/en-zh
IWSLT_PREFIX=train.tags.en-zh
IWSLT_FILE=${IWSLT_ROOT}/${IWSLT_PREFIX}.${LANG}

MOSESDECODER_ROOT=${TOOLS_DIR}/mosesdecoder
MOSESDECODER_TOKENIZER=${MOSESDECODER_ROOT}/scripts/tokenizer/tokenizer.perl

SACREMOSES_TOKENIZER=${TOOLS_DIR}/run_sacremoses.py
FAST_MOSESTOKENIZER_PY=${TOOLS_DIR}/run_fast_mosestokenizer.py
FAST_MOSESTOKENIZER=../build/rel/mosestokenizer

LINE_COUNTER=${TOOLS_DIR}/line_counter_w_timeout.py

.PHONY = help download


download:
	mkdir -p ${DATA_DIR} ${TOOLS_DIR}

	@echo "Downloading mosesdecoder"
	if [ ! -d ${MOSESDECODER_ROOT} ]; then \
		git clone https://github.com/moses-smt/mosesdecoder.git \
			${MOSESDECODER_ROOT}; \
	fi;

	@echo "Downloading IWSLT EN-ZH dataset"
	curl -C - -L -o ${DATA_DIR}/iwslt-en-zh.tgz \
		https://wit3.fbk.eu/archive/2017-01-trnted//texts/en/zh/en-zh.tgz
	tar -C ${DATA_DIR} -xvf ${DATA_DIR}/iwslt-en-zh.tgz

bench-tokenizer-perl:
	@echo "Running benchmark for tokenizer-perl"
	@mkdir -p ${OUTPUT_DIR}
	@head -n ${N} ${IWSLT_FILE} \
		| time ${MOSESDECODER_TOKENIZER} -q -a -no-escape -l ${LANG} \
		| ${LINE_COUNTER} -t ${TIMEOUT} \
		> ${OUTPUT_DIR}/bench-tokenizer-perl.${LANG}.out

bench-sacremoses:
	@echo "Running benchmark for sacremoses"
	@mkdir -p ${OUTPUT_DIR}
	@head -n ${N} ${IWSLT_FILE} \
		| time ${SACREMOSES_TOKENIZER} -a -x -l ${LANG} \
		| ${LINE_COUNTER} -t ${TIMEOUT} \
		> ${OUTPUT_DIR}/bench-sacremoses.${LANG}.out

bench-fast-tokenizer-py:
	@echo "Running benchmark for fast-tokenizer-py"
	@mkdir -p ${OUTPUT_DIR}
	@head -n ${N} ${IWSLT_FILE} \
		| time ${FAST_MOSESTOKENIZER_PY} -a -x -l ${LANG} \
		| ${LINE_COUNTER} -t ${TIMEOUT} \
		> ${OUTPUT_DIR}/bench-fast-tokenizer-py.${LANG}.out

bench-fast-tokenizer:
	@echo "Running benchmark for fast-tokenizer"
	@mkdir -p ${OUTPUT_DIR}
	@head -n ${N} ${IWSLT_FILE} \
		| time ${FAST_MOSESTOKENIZER} -a -x ${LANG} \
		| ${LINE_COUNTER} -t ${TIMEOUT} \
		> ${OUTPUT_DIR}/bench-fast-tokenizer.${LANG}.out

bench-all: \
	bench-tokenizer-perl \
	bench-sacremoses \
	bench-fast-tokenizer-py \
	bench-fast-tokenizer
