print("i am your custom ride planner")
print("let me plan a ride for you today")
print("options:")
print("1=car")
print("2=bike")
print("chose one")
choice=int(input())
if choice==1:
    print("nice choice")
    print("chose your car")
    print("1=suv")
    print("2=sedan")
    cartype=int(input())
    if cartype==1:
        print("speed = 100kmph")
        print("seats = 4")
        print("road = offroad trails")
    else:
        print("speed = 80kmph")
        print("seats = 5")
        print("road = city roads")
elif choice==2:
    print("nice choice")
    print("chose your bike")
    print("1=scooty")
    print("2=mountain bike")
    biketype=int(input())
    if biketype==1:
            print("speed = 60kmph")
            print("road = city roads")
    else:
            print("speed = 80kmph")
            print("road = offroad trails")
else:
     print("choice invalid")
     print("please try again")
print("ENJOY YOUR AMAZING RIDE")
print("THANK YOU!")