#!/bin/bash

DIR=$(basename "$PWD")

if [ $DIR != "doc" ]; then
	echo "You must run build.sh inside the 'doc' folder!"
	exit
fi

sphinx-build ./source/ ../docs