#define a class circle with instance object radius also define get area and get circumference to print the values 

class circle:

    def get_area(self,radius):
        self.radius = radius
        print(3.142*radius*radius)
    def get_circumference(self,radius):
        self.radius = radius
        print(2*3.141*radius)

s1=circle()
s1.get_area(5)
s1.get_circumference(5) 
