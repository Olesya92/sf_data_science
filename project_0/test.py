# import numpy as np
# print(np.uint8(-456))
# import numpy as np
# arr = np.array([1,5,2,9,10])
# print(arr)
# Перечислить список из списков можно
# было и в одну строку, но на нескольких
# строках получается нагляднее
# nd_arr = np.array([
#                [12, 45, 78],
#                [34, 56, 13],
#                [12, 98, 76]
#                ])
# print(nd_arr)
# # array([[12, 45, 78],
# #        [34, 56, 13],
# #        [12, 98, 76]])
# arr = np.array([1,5,2,9,10])
# print(arr.dtype)
# arr = np.array([1,5,2,9,10], dtype=np.int8)
# nd_arr = np.array([
#                [12, 45, 78],
#                [34, 56, 13],
#                [12, 98, 76]
#                ], dtype=np.int16)
# print(arr.ndim)
# 1
# print(nd_arr.ndim)
# 2
# print(arr.size)
# 5
# print(nd_arr.size)
# 9
# print(arr.itemsize)
# 1
# print(nd_arr.itemsize) #в arr хранятся числа в виде int8 (8 бит => 1 байт), а в nd_arr — в виде int16 (16 бит => 2 байта).
# 2

#Создадим одномерный массив из пяти элементов:
# zeros_1d = np.zeros(5)
# print(zeros_1d)

#Создадим трёхмерный массив с формой 5x4x3 и типом float32:
# zeros_3d = np.zeros((5,4,3), dtype=np.float32)
# print(zeros_3d.shape)

#создание массива из 60 чисел от -6 до 21 включительно
# arr = np.linspace(-6, 21, 60, endpoint=True)
# print(arr)
#узнать шаг
# np.linspace(-6, 21, 60, retstep=True, endpoint=True)

#меняем форму массива
# arr = np.arange(8)
# print(arr)
# arr.shape = (2, 4)
# print(arr)

#обращение к элементу по индексу
# arr = np.linspace(1, 2, 6)
# print(arr)
# print(arr[2])

#создание двумерного массива из одномерного
# nd_array =  np.linspace(0, 6, 12, endpoint=False).reshape(3,4)
# print(nd_array)
# print(nd_array[1, 2]) #число из 2 строки и 3 столбца
# arr = np.arange(6)
# print(arr)
# # [0 1 2 3 4 5]
# print(np.random.shuffle(arr))

# from statistics import mean 
# simplelist = [19, 242, 14, 152, 142, 1000]
# print(mean(simplelist )) #среднее значение списка
import pandas as pd
print(pd.__version__)
print(pd.__name__)