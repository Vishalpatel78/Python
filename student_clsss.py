class student:
    def getdata(self,name,rollno ,branch):
        self.name = name
        self.rollno= rollno
        self.branch = branch 
    def showdata(self):
        print(self.name )
        print(self.rollno )
        print(self.branch)

s1 = student()
s1.getdata("vishal",183,"cse")
s1.showdata()