text = input("Enter string ")

consonants = "bcdfghjklmnpqrstvwxyz"
count = 0

for char in text.lower():  
    if char in consonants:
        count += 1

print(f"Count: {count}")