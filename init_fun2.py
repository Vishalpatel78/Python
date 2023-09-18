class test:
    i = 10
    def __init__(self) -> None:
        print("init")
    def f1(self):
        print("hello")
        print(self.i)
t1= test()
t1.f1()