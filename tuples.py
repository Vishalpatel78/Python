# creating a tuple

tup = (4,5,6,8)
print(type(tup), tup)
print("length of the tuple is :", len(tup))
      
print(tup[0])
print(tup[1])
print(tup[2])

if 6 in tup:
    print("yes")

else:
    print("No")

# slising in tuple

tup2 = tup[1:4]
print(tup2)
