#tuples! ordered, immutable, allow duplicates

mytuple = "Max", 28, "Biggle", 632.32
print(type(mytuple))
print(mytuple)
print(type(mytuple[3]))
print(type(mytuple))

item = mytuple[0]
print(type(item))

for i in mytuple:
	print(i)


if "Max" in mytuple:
	print("Yes")
else:
	print("no")

my_tuple = 'a','b','c','d','e','f'
print(len(my_tuple))
print(my_tuple.count('a'))


print(my_tuple.index('d')) #return index of first instance

#convert to list and vice versa

my_list = list(my_tuple)
print(my_list)

mytuple2 = tuple(my_list)
print(my_list)

#slicing tuples

b = mytuple[0:3]
print(b)

b = mytuple[0:1]
print(b)

b = mytuple[::-1] #could reverse the tuple like this
print(b)

one, two, three, four = mytuple
print(one)
print(two)
print(three)
print(four)

#which is more efficient? tuple or list

import sys
my_list = [0,1,2, "hello", True]
my_tuple = 0, 1, 2, "hello", True
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes") #so tuple is smaller 104bytes vs 88 bytes

import timeit

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=10000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=10000000))

