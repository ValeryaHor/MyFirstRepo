input_str = input("������� ����� ����� ������: ")
numbers = list(map(int, input_str.split()))

sum_even = 0
sum_odd = 0

for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

difference = sum_even - sum_odd
print(f"����� ������ �����: {sum_even}")
print(f"����� �������� �����: {sum_odd}")
print(f"�������� (������ - ��������): {difference}")