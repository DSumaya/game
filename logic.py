import random
from decouple import config

def play_game():
    min_number = 1
    max_number = 100
    attempts = 10
    capital = 100

    print(f"Угадайте число от {min_number} до {max_number}. У вас {attempts} попыток.")

    number_to_guess = random.randint(min_number, max_number)

    while attempts > 0:
        print(f"Ваш текущий капитал: {capital}")
        bet = int(input("Введите вашу ставку (сумму): "))

        if bet > capital:
            print("У вас недостаточно средств для этой ставки!")
            continue

        guessed_number = int(input("Введите ваше предположение: "))

        if guessed_number == number_to_guess:
            capital += bet  # Удвоить ставку
            print(f"Поздравляем! Вы угадали число {number_to_guess}. Ваш капитал теперь: {capital}")
            break
        else:
            capital -= bet  # Потерять ставку
            attempts -= 1
            print(f"Неправильно. Осталось попыток: {attempts}. Загаданное число было {number_to_guess}.")

        if attempts == 0:
            print("Вы исчерпали все попытки. Игра окончена.")
