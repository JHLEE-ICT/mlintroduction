from collections import Counter

word = Counter()

f = open("C:\Users\lghld\Downloads\text.txt",'r')
#한줄한줄 string의 형태로 list로 저장해 넘겨주는 함수
lines = f.readlines()

for line in lines:
    for word in line.split():
        word[word]+=1


#빈도 수 확인
