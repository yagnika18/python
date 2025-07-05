class Human():
    def __init__(self):
        self.num_eyes=2
        self.num_nose=1
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class Male(Human):
    def __init__(self,name):
        super().__init__()
        self.name=name
        
    def sleep(self):
        print("i can sleep")
    def work(self):
        super().work()
        print("i can code")
male1=Male("Akash")
male1.eat()
male1.sleep()
male1.work()
print(male1.num_eyes)
print(male1.name)
