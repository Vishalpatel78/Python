s = { 5, 3,5,33,"vishal", 5.8,44}
for value in s:
    print(value)

# set are unordered collection of data items
# we can not find items in a set using index

s1 = { 1,2,3,4}
s2 = { 3,4,5,6}
print(s1,s2)

# update s1
s1.update (s2)
print(s1,s2)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))

# one set is disjoint if there are no itemss of given set are present in another one

p1 = { 30,40 }
p2 = { 30, 40, 50,60 }

print(p1.isdisjoint(p2))
print(p1.issuperset(p2))
print(p1.issubset(p2))