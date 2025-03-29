a = [1, 5, 6, 7, 8, 3, 2, 9, 4, 10]
b = [1, 2, 3]
c = [50, 76, 65, 4, 26, 107]


def bubble_sort1(lst: list):
    """Данная функция осуществляет сортировку по возрастанию
     элементов списка методом пузырька"""
    while True:
        key = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i + 1], lst[i]  = lst[i], lst[i + 1]
                key = False
        if key:
            break


def bubble_sort2(lst: list):
    """Данная функция осуществляет сортировку по возрастанию
     элементов списка методом пузырька"""
    for i in range(len(lst)):
        key = True
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j]  = lst[j], lst[j + 1]
                key = False
        if key:
            break
    return lst

bubble_sort2(a)
bubble_sort2(b)
bubble_sort2(c)
print(a)
print(b)
print(c)
