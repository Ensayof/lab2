def get_number():
    for i in range(30):
        if i % 2 != 0:
            yield i

generator = get_number()

res = []

for index, number in enumerate(generator, start=1):
    if index == 1 or index == 5 or index == 15:
        res.append(number)

print(f"Первое нечетное число: {res[0]}, Пятое нечетное число: {res[1]}, Последнее нечетное число: {res[2]}")