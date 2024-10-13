import random

numbers = random.sample(range(0, 201), 10)

x = int(input("Введите число x: "))

krat_x = list(filter(lambda num: num % x == 0, numbers))

print(f"Сгенерированный список: {numbers}")
print(f"Числа, кратные введенному числу{x}: {krat_x}")