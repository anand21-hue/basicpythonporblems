def factorial(num):
    if num<=0:
        return"not define"
    facto=1
    for i in range(1,num+1):
        facto=facto*i
    return facto
number=int(input("enter the number:"))
result=factorial(number)
print("factorial is:",result)
