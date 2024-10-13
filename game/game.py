import random

def game():
    choices = ['камень', 'ножницы', 'бумага']
    
    print("Выберите:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice.capitalize()}")
    
    try:
        user_choice_index = int(input("Введите номер вашего выбора: ")) - 1
        if user_choice_index not in range(3):
            print("Некорректный выбор!")
            return
    except ValueError:
        print("Введите число!")
        return

    user_choice = choices[user_choice_index]
    computer_choice = random.choice(choices)

    print(f"Вы выбрали: {user_choice}, а компьютер выбрал: {computer_choice}")
    
    # Определение победителя
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        print("Вы победили!")
    else:
        print("Победу одержала машина!")

game()