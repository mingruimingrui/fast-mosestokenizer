#!/bin/sh
set -e

for i in $(seq 5); do
    echo "######## RUN $i"
    make bench-all $@
    echo "####################"
done
