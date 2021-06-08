#dictionaries : key-value pairs, unordered, mutable

mydict = {"name": "Max", "age": 28, "City": "New York"}

print(mydict)

mydict2 = dict(name="Mary", age="40", city="Chester")
print(mydict2)

value = mydict["name"] #get value for a key
print(value)

#add something

mydict["email"] = "max@google.com"
print(mydict)

#delete something

del mydict["name"]
print(mydict)

ageout = mydict.pop("age")
print(mydict)
print(ageout)

#is it there? 

if "name" in mydict2:
	print(mydict2["name"])

try:
	print(mydict["name"])
except:
	print("Error!")

#loop thru



for key in mydict2:
	print(key)

for value in mydict2.values():
	print(value)

for key, value in mydict2.items(): #loop thru printing both key and the item
	print(key, value)

mydict_copy = mydict.copy()

#merging dictionaries

#mydict.update(mydict2)
#print(mydict)

#with tuples. but no lists
mytuple = (3, 7)
tupledict = {mytuple: 15}
print(tupledict)
