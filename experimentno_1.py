#write a program to create a class account which contains the attributes name, age , and address / 
#also define the displat function to print all the attrivutes

class account:
    def get_data(self, name , age, address):
        self.name = name
        self.age = age 
        self.address = address

    def display(self):
        print(self.name)
        print(self.age)
        print(self.address)

s1=account()
s1.get_data("vishal", 19, "bhopal")
s1.display()