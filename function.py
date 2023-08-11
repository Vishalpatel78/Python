def fun1(a,b):  # def is use for function declaration 
    if(a>b):
        print("Value a is greater ")
    else:
        print("Value b is greater of equal")
    
    print("Sum of the values is :", a+b)

print("here we call this function")
x = 10
y = 20
fun1(x,y)
m = 55
n = 323
fun1(m,n)



def avg(n,a,b,c):
   # n = int( input("Enter value of n"))
   # a = int(input("Enter value of a"))
    #b = int (input("Enter value of b"))
    c# = int(input("Enter value of c"))
    avg = (a + b +c)/n
    print("avg is :", avg)

avg(3,5,4,3)