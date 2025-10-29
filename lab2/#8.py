input_str = input("Enter with space: ")
numbers = list(map(int, input_str.split()))

result = [x for x in numbers if x % 5 != 0]
print(f"Result: {result}")
