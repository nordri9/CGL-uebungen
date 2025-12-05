#!/bin/sh

for i in {0..3}; do
    pandoc sheet0$i.md -o sheet0$i.pdf

done