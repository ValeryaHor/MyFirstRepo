input_str = input("Ââåäèòå ÷èñëà ÷åðåç ïðîáåë: ")
numbers = list(map(int, input_str.split()))

sum_even = 0
sum_odd = 0

for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

difference = sum_even - sum_odd
print(f"Ñóììà ÷¸òíûõ ÷èñåë: {sum_even}")
print(f"Ñóììà íå÷¸òíûõ ÷èñåë: {sum_odd}")
print(f"Ðàçíîñòü (÷¸òíûå - íå÷¸òíûå): {difference}")
