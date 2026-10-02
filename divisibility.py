print("ENTER ANY NUBMER(NUMERATER)")
numn=int(input())
print("ENTER ANY NUMBER(DENOMINATER)")
numd=int(input())
rem=numn%numd
if rem==0:
    print(numn,"is divisible by",numd)
else:
    print(numn,"is not divisible by",numd)