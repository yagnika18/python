def prime_checker(number):
    is_prime=True
    if number==1:
        is_prime=False
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime:
        print("it is prime")
    else:
        print("not a prime")
n=int(input("enter a number:\n"))
prime_checker(n)