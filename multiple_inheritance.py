class Human:
    #for attributes
    def __init__(self):
        self.num_eyes=2
        self.num_nose=1
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class Male:
    def __init__(self,name):
        self.name=name
    def sleep(self):
        print("i can sleep")
    def work(self):
        print("i can code")
class child(Human,Male):
    def __init__(self,name,language):
        Human.__init__(self)
        Male.__init__(self,name)
        self.language=language  #for accessing the language
    def communitate(self):
        print("i can communicate")
    def work(self):
        super().work()
        print("i can test")
    def display(self):
        print("hi i am {}".format(self.name))
obj=child("Yagni","python")
obj.sleep()
obj.work()
Male.work(obj)
print(obj.num_nose)
print(obj.name)
print(obj.language)
print(obj.display())#hi i am yagni none bze it is printing statement
obj.display() #i am yagni