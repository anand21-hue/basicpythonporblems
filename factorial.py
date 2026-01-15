num=int(input("enter the number:"))
# Factorial is not defined for negative numbers

if num<0:
    print("Factorial is not defined for negative numbers")
else:
    pn=1
    for i in range(1,num+1):
        pn=pn*i
    print("factor of",num,"is",pn)
