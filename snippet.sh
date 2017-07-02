#!/bin/bash -eu

font_size=$(( ${2-30} * 2 ))
pygmentize -f rtf -O "style=monokai,fontface=Menlo" $1 |sed "s/\\f0/\\f0\\\\fs$font_size/g" | pbcopy
