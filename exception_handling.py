# a = input("Enter the value")
# print(f"print the table of: ",{a})

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} * {i} = { int(a) * i}")

# except Exception as e:
#     print(e)

# finally:   
#     print("this is very important code ")
#     print("this is code for error handling")

# 2.create error

a = int(input("Enter the value between 5 to 10"))

if(a<5 or a>10):
    raise ValueError("This is a value error because user enter wrong value")

print("this is trial")
