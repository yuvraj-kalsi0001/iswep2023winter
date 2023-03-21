#!/bin/bash

for FILE in *.gff
do
	perl -p -e 's/ID=+(\w+)/$1/' $FILE > "$FILE.gff"
	perl -p -e 's/(\w+);.*/$1/' $FILE.gff > $FILE.gff.gff 
done

