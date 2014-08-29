#!/bin/sh

for i in `ls test_data/surface`
do
  python src/extract_links.py "test_data/surface/$i"
  echo "done processing $i"
done
