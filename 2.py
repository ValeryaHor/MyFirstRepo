numbers = list(map(int,input("Enter list ").split()))
i = 0
while (i < len(numbers)):
    if (numbers[i] % 2 == 0):
        numbers.pop(i)
    else:
        i += 1
print(numbers)  