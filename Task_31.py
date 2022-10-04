# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
def newNum(n):
    if n == 1:
        return 1
    else:
        return round((1 +2/n * 2)**n)

num = int(input("Введите число: "))

list = []
for i in range(1, num+1, 1):
    list.append(newNum(i))
sum = 0     
print(list)
print('На нечетных позициях: ')
for i in range(1, num, 2):
    sum = sum + list[i]
    print(list[i], end=' ')
print()
print(f'сумма которых равна {sum}')





# def mix(array):
#     for j in range(0, len(array)):
#         rnd = int(random.randrange(0, len(array)))
#         temp = listr[j]
#         listr[j] = listr[rnd]
#         listr[rnd] = temp
#     return array

# listr = list
# listmix = mix(listr)
# print(listmix)

