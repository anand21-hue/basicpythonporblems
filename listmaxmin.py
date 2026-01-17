numbers = list(map(int, input("Enter numbers separated by space: ").split()))
maximum = numbers[0]
minimum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Maximum value:", maximum)
print("Minimum value:", minimum)
