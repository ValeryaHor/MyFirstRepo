
input_str = input("Enter: ")
strings = tuple(s.strip() for s in input_str.split())

longest_string = max(strings, key=len)
print(f"Longest string '{longest_string}'")
print(f"{len(longest_string)} symbols")