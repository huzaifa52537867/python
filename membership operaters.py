print("give your marks of these three subjects")
sub1=int(input())
sub2=int(input())
sub3=int(input())
tot=sub1+sub2+sub3
avg=int(tot/3)
vd=range(0,101)
if avg not in vd:
    print("invalid input.")
elif avg in range(81,101):
    print("you have got grade A")
elif avg in range(61,81):
    print("you have got grade B")
elif avg in range(41,61):
    print("you have got grade C")
else:
    print("you have failed!!!")