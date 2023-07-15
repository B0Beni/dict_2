# ввести 10 пар ключ-значения (типа str) в словарь
# вывести словарь
# вывести словарь в виде таблицы (реализовать отдельной функцией)
def print_dict_as_table(dictionary: dict):
    # ключ       |  значение
    # -------------------------
    # красный    |   б
    # зелёный    |   шш
    # чёрный     |   у
    print(' ключ        |  значение')
    print('-------------------------')
    for x in dictionary:    #цикл по всем ключам в словаре
        v = dictionary[x]   #извлекаем значение из словаря по ключу x
        print(f'{x:12} |    {v}')

def input_dict(n:int)->dict:
    d = {}
    print(f'введите {n} пар ключ - значение')
    for i in range(n):
        s1, s2 = input().split()
        d[s1] = s2  # добавление пары ключ-значение в словарь
    return d


d = input_dict(2)
#print(d)
print_dict_as_table(d)
