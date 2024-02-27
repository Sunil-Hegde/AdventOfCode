#!/bin/bash

a=1
while [ $a -lt 26 ]
do
    touch day$a/README.md
    a=$((a + 1))
done
