#lists

mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)

item = mylist[0]
print(item)

for i in mylist:
	print(i)

if "banana" in mylist:
	print("yes")
else:
	print("no")

print(len(mylist))

mylist.append("lemon")

print(len(mylist))

mylist.insert(0, "blueberry")

print(len(mylist))

for i in mylist:
	print(i)

item = mylist.pop() #return and remove last item
print(item)
print(mylist)

item = mylist.remove("cherry") 
#item = mylist.clear() #remove everything in the list

item = mylist.reverse()
print(mylist)

new_list = sorted(mylist)
print(new_list)

list2 = [1,3,5,77,34,2,90,10]
print(list2)

#sort it
list2.sort()
print(list2)

#lists with multiples of the same thing in them

list3 = [1] * 5
print(list3)

list3 = ["Hello"] *5
print(list3)

anotherlist = list2 + list3
print(anotherlist)

#slicing bits of lists

print(list2)
a = list2[0:3] #range 0 to 3 so gets 0, 1, 2
print(a)

list_cpy = list2.copy() #copy method
print(list_cpy)

#list comprehension create new from existing list

a = [1,2,3,4,5,6]
b = [i*i for i in a] # new list with squares of the numbers in a
print(b)