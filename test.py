list = [8,9,10]

"""
문제 (a)
"""

list[1] = 17
#print(list)

"""
문제 (b)
"""

list.append(4)
list.append(5)
list.append(6)
#print(list)

"""
문제 (c)
"""

del list[0]
#print(list)

"""
문제 (d)
"""
list.sort()
#print(list)

"""
문제 (e)
"""

list = list*2
#print(list)

"""
문제 (f)
"""
list.insert(3,25)
print(list)