# in for loop 

# for i in range(5):
#     print(i)

# in while loop 

# i = 0
# while( i<5):
#     print(i)
#     i = i+1

# i = 5
# while(i>0):
#     print(i)
#     i = i-1

# use of break and continue

# for i in range(15):
#     if ( i==10):
#         break
#     print("5 X ",i+1,"=", 5* (i+1))


for i in range(15):
    if ( i==10):
        print("skip the itration for this number")
        continue
    print("5 X ",i+1,"=", 5* (i+1))