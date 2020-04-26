import numpy as np


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1

    left_edge = 0
    right_edge = 100

    predict = (right_edge - left_edge) // 2
    while number != predict and right_edge > left_edge:
        count += 1
        if number > predict:
            left_edge = predict
        else:
            right_edge = predict
        predict = left_edge + (right_edge - left_edge) // 2

    print(str(number) + ":" + str(predict))
    return count  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# Проверяем
score_game(game_core_v2)
