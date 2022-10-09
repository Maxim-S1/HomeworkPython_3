# Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# N = int(input("Введите число: "))

# def fibo(N):
#     if N >= 0:
#        i = range(N + 1)
#        arr = [0, 1]
#        for j in i[2: ]:
#            arr.append(arr[j - 1] + arr[j - 2]) 
#        return arr[N]
#     else:
#        N = - (N - 1)
#        i = range(N + 1)
#        arr = [1, 0]
#        for j in i[2: ]:
#            arr.append(arr[j - 2] - arr[j - 1]) 
#        arr.reverse()
#     return arr[0]

# for i in range(- N, N + 1):
#    print(fibo(i), end=' ')


def fib(n):
    if n in [1, 2]:
        return 1
    if n < 0:
        return fib(-n) * (-1) ** (-n+1)
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Введите число: "))

for i in range(n):
    print(fib((-n + i)))
for i in range(n):
    print(fib(i))
