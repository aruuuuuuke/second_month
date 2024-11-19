import random
from decouple import config


def load_config():
    min_number = config('MIN_NUMBER', cast=int)
    max_number = config('MAX_NUMBER', cast=int)
    attempts = config('ATTEMPTS', cast=int)
    initial_capital = config('INITIAL_CAPITAL', cast=int)
    return min_number, max_number, attempts, initial_capital


def start_game():
    min_number, max_number, attempts, initial_capital = load_config()
    capital = initial_capital
    return min_number, max_number, attempts, capital


def play_turn(min_number, max_number, capital):
    bet = 0
    while True:
        try:
            bet = int(input(f"Сделайте ставку (максимум {capital}): "))
            if bet > capital:
                print("У вас недостаточно средств для этой ставки.")
            elif bet <= 0:
                print("Ставка должна быть положительным числом.")
            else:
                break
        except ValueError:
            print("Пожалуйста, введите число.")
    secret_number = random.randint(min_number, max_number)

    guess = 0
    while True:
        try:
            guess = int(input(f"Угадайте число от {min_number} до {max_number}: "))
            if min_number <= guess <= max_number:
                break
            else:
                print(f"Число должно быть в диапазоне от {min_number} до {max_number}. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число.")

    if guess == secret_number:
        capital += bet
        print(f"Поздравляем! Вы угадали число {secret_number}. Ваш капитал теперь {capital}.")
    else:
        capital -= bet
        print(f"Увы, вы не угадали. Загаданное число было {secret_number}. Ваш капитал теперь {capital}.")
    return capital


def end_game(capital):
    if capital > 0:
        print(f"\nИгра завершена. Ваш итоговый капитал: {capital} рублей.")
    else:
        print("\nВы проиграли все деньги. Попробуйте снова!")

