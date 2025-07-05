def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print( "leap_year")
            else:
                print( "not a leap_year")
        else:
            print( "leap_year")
    else:
        print( "not a leap_year")
year=int(input("enter a number"))
leap_year(year)
