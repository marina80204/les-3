#encoding: utf8

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
#


# def say_hello_2(name, age, city):
#     print(name, age , city)
# n = 'Василий'
# a = 21
# c = 'Москва'
#
# say_hello_2(n, a, c)


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

# def my_pow(x):
#     return x ** 2
# data = (1, 2, 3)
# # for num in data:
# #     print(my_pow(num))
# #
# # print(list(map(my_pow, data)))
#
# def my_filter(x):
#     return x > 0
# print(list(filter(my_filter, data)))


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

# def render_person(name, *args):
#     print(name)
#     print(*args)
# render_person('ivan', 10, 20, 30)
# print(max('zz', 'aaa', key = len))