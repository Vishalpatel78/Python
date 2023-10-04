
class publication:
    def getdata(self):
        self.tittle =input("Enter the tittle of the book:")
        self.price = int(input("Enter the price of the book :"))
    
    def putdata(self):
        print("tittle of the book is :", self.tittle)
        print("price of the book is :", self.price)
    

class book(publication):
    def getdata(self):
        self.count = int(input("Enter the page count of the book :"))
    
    def putdata(self):
        print("total count is :",self.count)

            



class cd(publication):
    def getdata(self):
        self.pt = int(input("Enter the playing time"))
    
    def putdata(self):
        print("playing time is:",self.pt)

print("give all details of the books")
pub = publication()
pub.getdata()
pub.putdata()
b = book()
b.getdata()
b.putdata()
c = cd()
c.getdata()
c.putdata()


