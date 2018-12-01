#!/bin/bash
#step 1 of project
#combine the first lines of the BLAST gene results from the alignment csv texts downloaded from BASH
#usage bash align.sh when in the Bioinformatics_Group_Project directory

for file in ./*.csv
do
head -n 1 $file >> alignfinal.txt
done

