# У вас есть список чисел, и ваша задача - отсортировать его по возрастанию.

# Декларативный стиль
lst = [3, 4, 3, 1, 2]
lst.sort()
print(lst)

# Императивный стиль
numbers = [5, 2, 8, 1, 3]
sorted_numbers = []

for num in numbers:
    if len(sorted_numbers) == 0:
        sorted_numbers.append(num)
    else:
        for i in range(len(sorted_numbers)):
            if num < sorted_numbers[i]:
                sorted_numbers.insert(i, num)
                break
            elif i == len(sorted_numbers) - 1:
                sorted_numbers.append(num)
                break

print("Отсортированный список:", sorted_numbers)

lst1 = [3, 5, 4, 1, 2]
for i in range(len(lst1)):
    for j in range(i+1, len(lst1)):
        if lst1[i] > lst1[j]:
            lst1[i], lst1[j] = lst1[j], lst1[i]

print(lst1)