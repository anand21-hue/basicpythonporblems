text=input("enter a text:")
rev=""
for ch in text:
    rev=ch+rev
if rev==text:
    print("palindrome")
else:
    print("not palindrome")
