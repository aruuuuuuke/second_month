import logic


def main():
    min_number, max_number, attempts, capital = logic.start_game()
    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Ваш начальный капитал: {capital} рублей")
    print(f"Задание: Угадайте число от {min_number} до {max_number}")
    print(f"У вас {attempts} попыток. Удачи!")
    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt} из {attempts}. Ваш капитал: {capital} рублей")

        capital = logic.play_turn(min_number, max_number, capital)
        if capital <= 0:
            print("У вас закончились деньги. Игра окончена.")
            break
    logic.end_game(capital)


if __name__ == "__main__":
    main()
