print("===== MONEY DISPENSER====")
total100=total50=total20=total10=total1=0
served=0
dispensed=0
serving=True
while serving==True:
    name=input("enter your name.")
    amount=int(input(f"hi{name}how much do you want to withdraw"))
    if amount<=0:
        print("invalid amount,please enter a positive amount.")
        continue
    print("dispensing",amount,"for",name)
    index=1
    remaining=amount
    while index<=5:
        if index==1:
            note=100
        elif index==2:
            note=50
        elif index==3:
            note=20
        elif index==4:
            note=10
        else:
            note=1
        count=remaining//note
        if count>0:
          remaining=remaining-(count*note)
          if note==100:
                      total100+=count
          elif note==50:
                      total50+=count
          elif note==20:
                      total20+=count
          elif note==10:
                      total10+=count
          else:
                      total1+=count
        index=index+1
    served=served+1
    ans=input("any more customers?(yes/no)")
    if ans=="no":
           serving=False
print("transaction completed.")