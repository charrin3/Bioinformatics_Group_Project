#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:03:24 2018

@author: charrington
"""
import pandas
hitsframe1=pandas.read_csv("HMM_hits.txt",header=None)

linenumber=0
num_hits=0
name=""
finalhits=pandas.DataFrame(columns=['name','hits'])

for l in range(0,len(hitsframe1)):
    if l%2==0:
        name = hitsframe1.iloc[l, 0]
        num_hits = hitsframe1.iloc[l+1, 0]
        finalhits.loc[len(finalhits)]=[name, num_hits]
 

import numpy
import pandas
from plotnine import *

d=ggplot(finalhits,aes(x="name",y="hits"))+xlab("name")+ylab("hits")
d+geom_bar(stat="summary")

print (finalhits)


 
    

