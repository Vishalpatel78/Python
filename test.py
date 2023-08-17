# # d = { "vishal" : 90, "shrey": 40, "vivek": 95}
# # print(d)
# # d["nitin"] = 85
# # print(d)
# # p = d.values()
# # print(p)
# # for i in d:
# #     if i > 89:
# #         print(d[i])

# print(4 + 3 % 5)
# l = len(["hello",2, 4, 6])
# x = 100
# y = 50 
# print(x and y) 
# print(  2**(3**2) )
# print((2**3)**2)
# print((2**3**2 ))

# x = 1
# print(x<<2)

# # 

# list1 = [1,2,3,4]
# list2 = [2,4,5,6]
# list3 = [2,6,7,8]
# result = list()
# print(result.extend(i for i in list1 if i not in (list2+list3) and i not in result))
# print(result.extend(i for i in list2 if i not in (list1+list3) and i not in result))
# print(result.extend(i for i in list3 if i not in (list1+list2) and i not in result))


# # 
# L = [1, 23,‘hello’, 1].  
# 
a = 3

b = 1

print(a, b)

a, b = b, a

print(a, b)
