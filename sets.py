#sets unorded, mutable, NO DUPLICATES

myset = {1, 2, 3, 4, 5, 6, 7, 8}
print(myset)

myset2 = set("Hello!")
print(myset2)

#empty set has to be

myset2 = set()

myset2.add(1)
myset2.add(2)
myset2.add(3)

print(myset2)

myset2.remove(2)
#or myset2.discard(2)

print(myset2)

myset2.clear() #empty the set

print(myset2)

for i in myset: #iterate over elements
	print(i)

if 1 in myset:
	print("yes")

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

#union of odds and evens
u = odds.union(evens)
print(u)

#intersection of two sets i.e. elements found in both sets

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)

#difference of two sets

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)

diff = setB.symmetric_difference(setA) #so not 1,2,3 since in both sets
print(diff)

#modify sets in place

setA.update(setB) #add elements from the other set without duplication
print(setA)

setA.intersection_update(setB) #update with only elements found in both sets
print(setA)


setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1,2,3,10,11,12}
#remove elements that occured in the other set

#setA.difference_update(setB)
#print(setA)



#setA.symmetric_difference_update(setB)
#print(setA)

####

setA = {1,2,3,4,5,6}
setB = {1,2,3}

print(setB.issubset(setA)) 

print(setA.issuperset(setB))

print(setA.isdisjoint(setB)) #null intersection?


