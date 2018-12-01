#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:03:24 2018

@author: charrington
"""
import pandas
hitsframe1=pandas.read_csv("sequence1_hits.txt",header=None, sep=",")
hitsframe2=pandas.read_csv("sequence2_hits.txt",header=None, sep=",")
hitsframe6=pandas.read_csv("sequence6_hits.txt",header=None, sep=",")
hitsframe8=pandas.read_csv("sequence8_hits.txt",header=None, sep=",")
hitsframe9=pandas.read_csv("sequence9_hits.txt",header=None, sep=",")
hitsframe10=pandas.read_csv("sequence10_hits.txt",header=None, sep=",")

l=["control1", "control2", "obese1", "obese2"]

 

import numpy
import pandas
from plotnine import *

a=ggplot(hitsframe1,aes(x='hitsframe1.iloc[:,0]',y='hitsframe1.iloc[:,1]'))+xlab("sequence1")+ylab("hits")
g=a+geom_bar(stat="summary")+scale_x_discrete(labels=l)
ggsave(filename="sequence1hits.pdf", plot=g)


b=ggplot(hitsframe2,aes(x='hitsframe2.iloc[:,0]',y='hitsframe2.iloc[:,1]'))+xlab("sequence2")+ylab("hits")
g=b+geom_bar(stat="summary")+scale_x_discrete(labels=l)
ggsave(filename="sequence2hits.pdf", plot=g)

c=ggplot(hitsframe6,aes(x='hitsframe6.iloc[:,0]',y='hitsframe6.iloc[:,1]'))+xlab("sequence6")+ylab("hits")
g=c+geom_bar(stat="summary")+scale_x_discrete(labels=l)
ggsave(filename="sequence6hits.pdf", plot=g)

d=ggplot(hitsframe8,aes(x='hitsframe8.iloc[:,0]',y='hitsframe8.iloc[:,1]'))+xlab("sequence8")+ylab("hits")
g=d+geom_bar(stat="summary")+scale_x_discrete(labels=l)
ggsave(filename="sequence8hits.pdf", plot=g)

e=ggplot(hitsframe9,aes(x='hitsframe9.iloc[:,0]',y='hitsframe9.iloc[:,1]'))+xlab("sequence9")+ylab("hits")
g=e+geom_bar(stat="summary")+scale_x_discrete(labels=l)
ggsave(filename="sequence9hits.pdf", plot=g)

f=ggplot(hitsframe10,aes(x='hitsframe10.iloc[:,0]',y='hitsframe10.iloc[:,1]'))+xlab("sequence10")+ylab("hits")
g=f+geom_bar(stat="summary")+scale_x_discrete(labels=l)
ggsave(filename="sequence10hits.pdf", plot=g)







 
    

