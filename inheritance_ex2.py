class Person():
    def __init__(self,name,id_num):
        self.name=name
        self.num=id_num
    def display(self):
        print(self.name)
        print(self.num)
    #def details(self):
        #print("my name is {}".format(self.name))
        #print("my id_num is {}".format(self.num))
class Employee(Person):
    def __init__(self, name, id_num,address,salary):
        self.add=address
        self.sal=salary
        Person.__init__(self,name,id_num)
    def details(self):
        print("my name is {}".format(self.name))
        print("my id_num is {}".format(self.num))
        print("my address is {}".format (self.add))
obj=Employee("siv",1234,"delhi",20000)
obj.details()
obj.display()