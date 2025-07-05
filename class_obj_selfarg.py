class Instructor:
    def __init__(self,inst_name,inst_age):
        self.name=inst_name
        self.age=inst_age
        self.followers=0
instructor1=Instructor("yagnika",20)
print(instructor1.name)
print(instructor1.followers)
instructor2=Instructor("siva",22)
print(instructor2.age)