my_dict = {'one': 1, 'two': 200, 'ten': 10, 'twenty': 20}

filtered_dict = dict(filter(lambda item: item[1] >= 10, my_dict.items()))
print(f"Filtered {filtered_dict}")
