input1 = input("Enter set1: ")
set1 = set(map(int, input1.split()))


input2 = input("Enter set2 ")
set2 = set(map(int, input2.split()))

result = set1 ^ set2
print(result)