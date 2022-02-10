import random


a = []
b = []

def num_list(mas):
    for i in range(10):
        mas.append(random.randint(0, 20))
    return mas


num_list(a)
num_list(b)


def check(list1, list2):
    equal_list = [list1[i] for i in range(len(a)) if list1[i] in list2]

    return equal_list


print(check(a, b))