#collections: counter, namedtuple, ordereddict, defaultdict, deque

### COUNTER

from collections import Counter

a = "aaaaaabbbbcccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print("Most common:", my_counter.most_common(1))

print(list(my_counter.elements()))

from collections import namedtuple

Point = namedtuple('Point', 'x,y') #class point with fields x and y
pt = Point(1, -4) #give values
print(pt)
print(pt.x, pt.y)

from collections import OrderedDict #like regular dict but remembers order items inserted
#not much use now

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

from collections import defaultdict

#difference being it has a default value if key not set

d = defaultdict(int) #default type of int
d['a'] = 1
d['b'] = 2

print(d)
print(d['c']) #gives the default value since not exist


from collections import deque

d = deque()
d.append(1)
d.append(2)

d.appendleft(3)

print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.extend([4,5,6])
print(d)
d.extendleft([13,12,11])
print(d)

d.rotate(1) #all rotate one place to right
print(d)
d.rotate(-1) #all rotate one place to left

