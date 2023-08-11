dict = {
    "vishal" : "human",
    "beg"    : "item",
    "laptop" : "technical gadget",
    "dal chawal": "food item"
}
print(dict["vishal"])
print(dict.keys())


for key in dict:
    print(dict[key])

# methods of dictionary

z1 = { 1: 55, 2: 33, 3:64, 4:87}
z2 = { 11: 84, 12:93, 13:94, 14:83 }

# update method
z1.update(z2)
print(z1)

# clear item
z1.clear()
# empty dictionary
# empt = {}
# print(empt)


# pop 

# z1.pop(33)