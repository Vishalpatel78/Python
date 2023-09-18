Q = set("A","B","C","D","M")
F = set("D")
E = set("a","b")
q = "A"
 
a = int(input("ent input:"))
if(q =="A"):

     entry = input("enter step:")
     if(entry == "a"):
        q = "B"

        entry = input("enter step:")
        if(entry == "b"):
                q = "C"

                entry = input("enter step:")
                if(entry == "b"):
                    q = "D"
                    print("it is the final state:", q) 
                else:
                    print("wrong input:")
        else:
                print("you entered wrong input:")

     else:
            print("you entered wrong input:")
else:
    print("starting point is not valid:")

 
