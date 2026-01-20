def charfreq(text):
    freq={}
    for ch in text:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq
text=input("enter a string:")
result=charfreq(text)
print("character frequency:")
for key,value in result.items():
    print(key,":",value)
