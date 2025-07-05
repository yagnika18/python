def add(*numbers):
    c=0
    for i in numbers:
        c+=i
    print(f"sum is {c}")
add(2,4,3)
add(2,3,1,2)

def add(*numbers,name):
    c=0
    print(numbers)
    print(name)
    for i in numbers:
        c+=i
    print(f"sum is {c}")
add(1,2,name="vikram")


def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
info_person(name="ram",dept="IT",age=30)
info_person(name="syam",dept="cse")