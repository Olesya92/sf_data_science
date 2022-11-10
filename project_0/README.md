# Проект 0. Игра: Угадай число

## Оглавление  
[1. Описание проекта](https://github.com/Olesya92/sf_data_science/blob/main/project_0/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/Olesya92/sf_data_science/blob/main/project_0/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/Olesya92/sf_data_science/blob/main/project_0/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/Olesya92/sf_data_science/blob/main/project_0/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/Olesya92/sf_data_science/blob/main/project_0/README.md#Результат)    
[6. Выводы](https://github.com/Olesya92/sf_data_science/blob/main/project_0/README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число меньше, чем за 20 попыток.

:arrow_up:[к оглавлению](https://github.com/Olesya92/sf_data_science/blob/main/project_0/README.md#Оглавление)


### Какой кейс решаем?    
Написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число»
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на Python
Учимся работать с IDE
Учимся работать с GitHub

### Этапы работы над проектом  
В ходе реализации проекта был опробован алгоритм решения данной задачи c помощью метода бинарного поиска([код](https://github.com/Olesya92/sf_data_science/blob/main/project_0/game_v2.py))

:arrow_up:[к оглавлению](https://github.com/Olesya92/sf_data_science/blob/main/project_0/README.md#Оглавление)


### Результаты:  
По [результатам опробирования](https://github.com/Olesya92/sf_data_science/blob/main/project_0/game.ipynb) обоих алгоритмов установлено:
1. Алгоритм со случайным угадыванием и сокращением диапазона в среднем угадывал число с 8 попытки
2. Алгоритм, реализованный по методу бинарного поиска, в среднем угадывал число с 5 попытки

:arrow_up:[к оглавлению](https://github.com/Olesya92/sf_data_science/blob/main/project_0/README.md#Оглавление)


### Выводы:  
Метод бинарного поиска позволяет угадывать число за ниаменьшее число попыток.

:arrow_up:[к оглавлению](https://github.com/Olesya92/sf_data_science/blob/main/project_0/README.md#Оглавление)