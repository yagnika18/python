class Dog:
    attr1="mammal"#class attribute
    #instance attribute
    def __init__(self,name):
        self.name=name
#object instantiation
Dog_breed1=Dog("rodger")
Dog_breed2=Dog("tommy")
print(Dog_breed1.name)
#accessing class attributes
print("rodger is a {}".format(Dog_breed1.__class__.attr1))
print("tommy is a {}".format(Dog_breed2.__class__.attr1))
#accessisng instance attributes
print("My name is {}".format(Dog_breed1.name))
print("My name is {}".format(Dog_breed2.name))