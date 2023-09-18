import array as a

ar1 = a.array('i',[10,20,30,40,50])
ar2 = a.array('i',[15,20,25,40,55])

for i in range(0,5):
    if (ar1[i] == ar2[i]):
        print("index value is same",ar1[i])
    
    elif(ar1[i]>ar2[i]):
        print("array1 index is greater")

    else:
        print("index value is not same")

