# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

min = int(input("Введи минимальное значение: "))
max = int(input("А теперь максимальное: "))
my_list = [random.randint(1, 20) for _ in range(max + min)]
print(my_list)
if max <= min:
    print("Не мухлюй и введи правильно...")
else:
    for i in range(len(my_list)):
        if min <= my_list[i] <= max:
            print(f"[{i}]", end=" ")
