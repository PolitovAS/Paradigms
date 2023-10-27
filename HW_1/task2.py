# Задача №2
# Дан список целых чисел numbers. Необходимо написать в декларативном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.


def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

numbers = [5, 2, 7, 1, 3]
print("Отсортированный список:", sort_list_declarative(numbers))
print("Оригинальный список:", numbers)
