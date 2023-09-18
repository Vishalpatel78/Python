import array as a
ar = a.array('i',[1,2,3,4,6])

print(ar)
print("type of ar is :",type(ar))

print("third element of the array is :", ar[3])

ar.insert(3,55)
print("After inserting array is:",ar)

for i in ar:
    print(i)

print("length of array is ",len(ar))

ar.pop(5)
print(ar)

ar.remove(55)
print(ar)

points = [55,56,57]
ar.extend(points)
print(ar)