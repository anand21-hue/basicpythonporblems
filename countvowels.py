text=input("enter a string: ")
vow="aeiouAEIOU"
count=0
for ch in text:
    if ch in vow:
        count+=1
print("print number of vowels",count)
