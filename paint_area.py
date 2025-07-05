import math as m

def paint_cal(height,width,cover):
    area=height*width
    no_of_cans=m.ceil(area/coverage)
    print(f"yu will need {no_of_cans} cans of paint")


h=int(input("enter height of the wall in meters:"))
w=int(input("enter width of the wall in meters:"))
coverage=7
paint_cal(height=h,width=w,cover=coverage)