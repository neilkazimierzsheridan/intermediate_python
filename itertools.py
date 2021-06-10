#Itertools tools for handling iterators
#product permutations combinations accumulate groupby infinite iterators 

from itertools import product

a = [1,2]
b = [3]

prod = product(a,b, repeat=2) #cartesian product of iterables, can add repeats with repeat=x
print(list(prod))

from itertools import permutations #return all possible orderings
#which is quite useful really!


a = [1,2,3, 4]
perm = permutations(a)
print(list(perm))

from itertools import combinations
#return all possible combinations with specified length
a = [1,2,3,4]
com = combinations(a, 2) #2 being specified length

print(list(com))

from itertools import combinations_with_replacement

a = [1,2,3,4]
com = combinations_with_replacement(a, 2) #2 being specified length

print(list(com))


from itertools import accumulate
#iterator that returns accumulated sums

a = [1,2,3,4]

acc = accumulate(a)
print(a)
print(list(acc))

import operator 

#you don't have to sum, can for e.g. multiply
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))

from itertools import groupby 

def small_than_3(x):
	return x < 3

a = [1,2,3,4]
group_obj = groupby(a, key=small_than_3)

for key, value in group_obj:
	print(key, list(value))

# or

group_obj = groupby(a, key=lambda x: x<3)

for key, value in group_obj:
	print(key, list(value))


from itertools import count, cycle, repeat 

for i in count(10): #infinite loop starting at ten
	print(i)
	if i == 200:
		break

a = [1,2,3]

#for i in cycle(a): #cycle thru infinite 
	#print(i)
	

for i in repeat(a, 20): #repeat, second argument for stop e.g. how many repeats 
	print(i)
	