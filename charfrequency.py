text=input("enter the text")
freq={}
for ch in text:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print("character freq:")
for key,value in freq.items():
    print(key,":",value)
