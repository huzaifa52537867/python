field1=50
field2=25
field3=35
total=field1+field2+field3
average=total/3
print("total harvest:",total,"kg")
print("average:",average,"kg")
bags=20
no_of_bags=total//bags
leftover=total%bags
print("number of bags:",no_of_bags)
print("leftover:",leftover,"kg")
old_harvest=200
harvest=total>old_harvest
same=total==old_harvest
print("if the harvest is better:",harvest)
print("if harvest is same",same)
total+=15
print("harvest with bonus:",total)
total-=20
print("harvest after taking some out for next year:",total)
final_count=total//bags
print("total number of bags:",final_count)