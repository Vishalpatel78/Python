def fact(n):
    f=1
    while n>1:
        f=f*n
        n-=1
    return f
num=int(input("how many no you wants:  ") )   
for i in range(1,num+1):
    print('factorial of {} ={}'.format(i,fact(i)))
             
