num=int(input("Enter the number of terms: "))
# Fibonacci series is not defined for negative numbers
if num<= 0:
    print("Please enter a positive integer")
elif num== 1:
    print("Fibonacci series:")
    print(0)
else:
    a = 0
    b = 1
    print("Fibonacci series:")
    print(a, b, end=" ")
    for i in range(2, num):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
