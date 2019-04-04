#!/bin/bash

DIR=$(basename "$PWD")

if [ $DIR != "doc" ]; then
	echo "You must run build.sh inside the 'doc' folder!"
	exit
fi

if [ $# -eq 0 ]; then
	echo "No output folder supplied. Generating docs into '../docs'"
	OUTPUT_DIR='../docs'
else
	echo "Generating docs into '$1'"
	OUTPUT_DIR="$1"
fi

sphinx-build ./ "$OUTPUT_DIR"
