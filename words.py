# 단어 별로 분리
from string import punctuation

text = open('text.txt','r',encoding='utf-8').read()

text = text.lower()

for p in punctuation:
    text = text.replace(p,'')
words = text.split()

d = {}

for w in words:
    if w in d:
        d[w] = d[w] + 1
    else:
        d[w] = 1
        

items = list(d.items())
items = [(i[1],i[0]) for i in items]
items.sort()

for i in items:
    print(i)

f = open('writefile.txt','w+',encoding='utf-8')
for i in items:
    f.write(str(i))
    f.write("\n")
f.close()
