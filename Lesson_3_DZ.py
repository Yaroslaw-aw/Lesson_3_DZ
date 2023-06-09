﻿import random

# Задача 1. Создайте список. Запишите в него N первых
# элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def fibb():
    n = int(input('Введите число: '))
    fibb = [0, 1] 
    for i in range(2, n):        
        fibb.append(fibb[i-2] + fibb[i-1])
    print(fibb[:n])
    
# Задача 2. В списке находятся названия фруктов.
# Выведите все фрукты, названия которых начинаются
# на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

def fruits():
    letter = input('Введите букву: ').lower()
    fruits = ['абрикос', 'авокадо', 'апельсин', 'айва', 'банан', 'киви', 'фейхоа']
    for word in fruits:
        if word[0].lower() == letter:
            print(word, end=', ')

# Задача 3. Создайте скрипт бота, который находит ответы на фразы
# по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет»,
# «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.

def bot():
    answers = {"привет": "Привет!",
              "как тебя зовут?": "Ваш личный раб. Чего изволите, хозяин?"}
    flag = True
    while flag:
        question = input('Введите вопрос: ').lower()
        if question == "стоп":
            print('Я буду ждать вас, мой хозяин.')
            flag = False
        elif question in answers.keys():
            print(f'Ответ раба: ', answers[question])
        else:
            print(f'Ответ раба: ', 'Неизвестный вопрос. Как мне ответить на этот вопрос в следующий раз?')
            key = question
            answers[key] = input('Ответ в следующий раз: ') 