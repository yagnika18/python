def greet(name,dept):#name and dept are non-default arguments
    print(f"hi{name}")
    print(f"are u from{dept} department?")
greet("ram","it")#these are positional arguments where name as ram and dept as it
greet(dept="cse",name="sruthi")#keyword arguments
#keyword arugument should follow the positional argument
#greet ("ram",dept="it")
#default argument should be mentioned in the parament as example subject="c++" and should be followed by non-default
# if we call any sub then it overrides the default values

def add(*numbers):
    #here *not defined length then varible length be * and single * accepts only positional arguments
    c=0
    for i in numbers:
        c=c+i
        print(f"sum is {c}")
add(2,4,9)
add(23,9,6,1)
    