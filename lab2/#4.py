input_str = input("Enter list ")
numbers = list(map(float, input_str.split()))

average = sum(numbers) / len(numbers)
print("Average ", average)
