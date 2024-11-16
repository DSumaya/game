import random
from decouple import config

def game_play():
    min_number = config("MIN_NUMBER")
    max_number = config("MAX_NUMBER")
    attempts = config("ATTEMPTS")
    initial_capital = config("INITIAL_CAPITAL")

    print(f"Угадайте число от {min_number} до {max_number}. У вас {attempts} попыток.")

    number_to_guess = random.randint(min_number, max_number)

    while attempts > 0:
        print(f"Ваш текущий капитал: {initial_capital}")
        bet = int(input("Введите вашу ставку (сумму): "))

        if bet > initial_capital:
            print("У вас недостаточно средств для этой ставки!")
            continue

        guessed_number = int(input("Введите ваше предположение: "))

        if guessed_number == number_to_guess:
            initial_capital += bet  # Удвоить ставку
            print(f"Поздравляем! Вы угадали число {number_to_guess}. Ваш капитал теперь: {initial_capital}")
            break
        else:
            initial_capital -= bet  # Потерять ставку
            attempts -= 1
            print(f"Неправильно. Осталось попыток: {attempts}. Загаданное число было {number_to_guess}.")

        if attempts == 0:
            print("Вы исчерпали все попытки. Игра окончена.")




