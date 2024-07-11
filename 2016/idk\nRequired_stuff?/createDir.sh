#/bin/bash

a=1
while [ $a -lt 26 ]
    do
        mkdir ../day$a
        touch ../day$a/RAEADME.md
    a=`expr $a + 1`
done