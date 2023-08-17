# str = "welcome to \t the collage"
# print(str)


# str = "welcome to \r the collage"
# print(str)

# str = "welcome to \t the collage"
# print(str)


# str = "welcome to \b the collage"
# print(str)

# str = "welcome to \t the collage"
# print(str)


# str = "welcome to \\ the collage"
# print(str)


str = "core python"
l = len(str)
for i in range(0,l):
               print(str[i], end = " ")
print("\n")             
for i in range(l-1,-1,-1):
     print(str[i], end = ' ')