#write a pr to create a class with name student whose data members ars name enrolment num , age , branch , and semester and member 
#functions are putdata and get data create two obj take data for objects and print details

class student:
    def put_data(self, name , roll_no, age, branch,sem):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.branch = branch
        self.sem = sem
    def show_data(self):
        print(self.name)
        print(self.roll_no)
        print(self.age)
        print(self.branch)
        print(self.sem)
s1=student()
s2=student()
s1.put_data("vishal",183, 19, "cse", 5)
s2.put_data("shrey",161,19,"cse",5)
s1.show_data()
s2.show_data() 

