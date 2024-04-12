'''
1. Написать функцию, которая принимает на вход список целых чисел
и возвращает новый список, содержащий только уникальные элементы из исходного списка.
'''


def task1(input_list):
    return list(set(input_list))


'''
2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) 
и возвращает список всех простых чисел в заданном диапазоне.
'''


def task2(min, max):
    output_list = []
    for i in range(max, min, -1):
        if i < 2:
            break
        flag = 0
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            output_list.append(i)
    return list(reversed(output_list))


'''
3. Создать класс Point, который представляет собой точку в двумерном пространстве. 
Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки, 
а также для получения и изменения координат.
'''


class Task3:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def distance(self, point):
        return ((self.__x - point.__x) ** 2 + (self.__y - point.__y) ** 2) ** 0.5


'''
4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
'''


def task4(input_list):
    input_list.sort(key=list)
    print(input_list)
    print(list(reversed(input_list)))
