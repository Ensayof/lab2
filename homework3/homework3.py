def calculate_age():

    dateb = input("Введите дату рождения в формате день/месяц/год: ")

    try:
        parts = dateb.split('/')
        if len(parts) != 3:
            raise ValueError("Неверный формат ввода. Должно быть три значения, разделенных '/'.")
        
        day, month, year = map(int, parts)

        if day < 1 or day > 31:
            print("Неверный день. Попробуйте снова.")
            return
        if month < 1 or month > 12:
            print("Неверный месяц. Попробуйте снова.")
            return
        if year > 2024:
            print("Неверный год. Попробуйте снова.")
            return

        now_day = 13
        now_month = 10
        now_year = 2024

        age = now_year - year
        if (now_month, now_day) < (month, day):
            age -= 1
        print(f"Ваш возраст: {age}")

    except ValueError:
        print("Неверный формат ввода. Убедитесь, что ввели числа в формате день/месяц/год.")

calculate_age()