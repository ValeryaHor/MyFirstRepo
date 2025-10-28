input_str = input("Введите числа через пробел: ")
numbers = list(map(int, input_str.split()))

sum_even = 0
sum_odd = 0

for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

difference = sum_even - sum_odd
print(f"Сумма чётных чисел: {sum_even}")
print(f"Сумма нечётных чисел: {sum_odd}")
print(f"Разность (чётные - нечётные): {difference}")