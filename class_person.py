class person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def showdata(self):
        print(self.name)
        print(self.age)
    
s1 = person()
s1.getdata("vishal", 19)
s1.showdata()

