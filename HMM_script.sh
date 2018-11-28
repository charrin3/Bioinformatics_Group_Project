#!/bin/bash
#Build HMM for each 6 transcript proteins and search the 4 translated RNAseq files
#usage: bash HMM_script.sh

#muscle alignments
for i in *sequence*
do
~/muscle3.8.31_i86linux64 -in $i -out $(basename -s .fasta "$i").txt
done

#HMM 
for j in *.txt
do
~/local/bin/hmmbuild $(basename -s .txt "$j").hmm $j
done

for file_search in "Control1protein.fasta" "Control2protein.fasta" "Obese1protein.fasta" "Obese2protein.fasta"
do
for file_build  in *.hmm
do
~/local/bin/hmmsearch --tblout $(basename -s .fasta "$file_search")_search.txt $file_build $file_search
done
done

