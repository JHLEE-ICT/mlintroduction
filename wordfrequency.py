# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:51:39 2019

@author: JIHYUN
"""

from string import punctuation

text = open('text.txt','r',encoding = 'utf-8').read()
text = text.lower()

for i in punctuation:
    text = text.replace(i,'')
words = text.split()

d = {}
for i in words:
    if(i in d):
        d[i] = d[i]+1
    else:
        d[i] = 1

items = list(d.items())
items = [(i[1],i[0]) for i in items]
items.sort()

for i in items:
    print(i)
    
f = open("words_frequency.txt","w",encoding = 'utf-8')
for i in items:
    f.write(str(i))
    f.write("\n")
f.close()