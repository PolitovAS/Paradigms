# imperative paradigm
n = int(input())

for i in range(1, n+1):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j)


"""Выбор парадигмы обосновывается тем, что задача требует простых итераций по двум переменным 
(от 1 до n и от 1 до 9), что легко реализуется в императивной парадигме с помощью циклов. 
Данная задача не требует использования сложных алгоритмов или структур данных.
"""