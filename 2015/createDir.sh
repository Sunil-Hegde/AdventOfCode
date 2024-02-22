#/bin/bash

a=2
while [ $a -lt 26 ]
    do
        mkdir day$a
    a=`expr $a + 1`
done