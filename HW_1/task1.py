# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative_first_method(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def sort_list_imperative_second_method(numbers):
    sorted_numbers = []

    for num in numbers:
        if len(sorted_numbers) == 0:
            sorted_numbers.append(num)
        else:
            for i in range(len(sorted_numbers)):
                if num > sorted_numbers[i]:
                    sorted_numbers.insert(i, num)
                    break
                elif i == len(sorted_numbers) - 1:
                    sorted_numbers.append(num)
                    break
    return sorted_numbers


numbers = [5, 2, 7, 1, 3]
print("Оригинальный список:", numbers)
print("Отсортированный список первым методом:", sort_list_imperative_first_method(numbers))
print("Отсортированный список вторым методом:", sort_list_imperative_second_method(numbers))

