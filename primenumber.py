num=int(input("enter a number:"))  # in this step we can initialize the number
if num<=1:  #if number is 1 or 0 or negative there not prime numbers 
    print("not prime") 
else:  
    for i in range (2,int(num**0.5)+1):  # We check divisibility only up to square root for efficiency

        if num%i==0:
            print("not prime")
            break
    else:
        print("prime")
