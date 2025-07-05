class Parent:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class Child(Parent):
    def sleep(self):
        print("i can sleep")
class Grandchild(Child):
    def work(self):
        #Parent.work(self)
        super().work()
        print("i can code")
obj=Grandchild()
obj.work()