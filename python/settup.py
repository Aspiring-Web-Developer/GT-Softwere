score=(10,20,30,20,20)

print(score.index(20))
print(score.count(20))
print(len(score))

# a=list(score)
c={}#dic

b=set()
b.add(2)
print(b)

setval={1,2,3,3,4,5,5,7}
print(setval)

setval.add(999)
print(setval)

setval.remove(1)#if present it wil rmove otherwise itll throw error
print(setval)

setval.discard(5)#if present it wil rmove otherwise it wont throw error
print(setval)

setval.pop()
print(setval)


c={1,2,3,4,5}
d={3,4,5,6,7}
e={3,4,5}

print('intesection',c.intersection(d))
print('union',c.union(d))

print(c.difference(d))

print(c.isdisjoint(d))
print(e.issubset(d))


