"""Игра угадай число.Компьютер сам загадывает и угадывает число"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly giess a number

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attemps
    """

    count = 0
    start = 1
    end = 100
    while True:

        count += 1
        predict_number = (start+end) // 2 # метод бинарного поиска
        if predict_number == start:
            return(count) 
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number < predict_number:
            end = predict_number
        else:
            start = predict_number     
    return(count)

def score_game(random_predict) -> int:
    """For how many attempts on average out of 1000 approaches does our algorithm guess

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))   
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
#RUN
if __name__ == '__main__':
    score_game(random_predict)