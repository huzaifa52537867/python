print("answer these three question and i will plan your day!")
day=input("which day is it today?(monday/sunday)")
weather=input("what is the weather today?(sunny/rainy/cloudy)")
homework=input("have you completed your homework?(yes/no)")
if day=="sunday":
    print("its a weekend,enjoy your favorite show")
elif day=="monday":
    print("its weekday,go to school")
elif day=="tuesday":
    print("its a normal day")
elif day=="wednesday":
    print("its a normal day")
elif day=="thursday":
    print("its a normal day")   
elif day=="friday":
    print("its the last weekday")
elif day=="saturday":
    print("its a holiday,enjoy")
else:
    print("day is not recognised")
if weather=="sunny"and homework=="yes":
    print("go to the park and play")
if weather=="rainy"or homework=="no":
    print("stay indoors and enjoy your favorite show")
if not weather=="sunny":
    print("you might want to carry an umbrella")
if not(homework=="yes")and weather=="sunny":
    print("finish your home work and go to play")
