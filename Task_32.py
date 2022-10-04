#  Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и
#  последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


number = [1, 2, 8, 6, 11, 7, 12, 15]
print(number)

if len(number) % 2 == 0:
    for i in range(0, int(len(number)//2)):
        N = number[i] * number[len(number)- i - 1]
        print(N, end=' ')        
else: 
    for i in range(0, int(len(number)//2 + 1)):
        N = number[i] * number[len(number)- i - 1]
        print(N, end=' ') 
    