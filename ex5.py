i = int(input('Введите число '))

sum = 0


while i > 0:
    num = i % 10
    sum = sum + num
    i = i // 10

print(f'Сумма {sum}')