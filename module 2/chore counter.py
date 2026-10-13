chorenum=3
task=1
completed=0
total=chorenum
while task<=chorenum:
    if task==1:
        nextchore="wash the dishes"
    elif task==2:
        nextchore="walk your dog"
    else:
        nextchore="make your bed"
    ans=input(f"have you finished'{nextchore}'(yes/no)")
    if ans=="yes":
        task+=1
        print("nice work,now do the next task")
        completed+=1
    else:
        print("try doing the task")
    remaining=total-completed
    print("remaining task:",remaining)
print("all task completed")