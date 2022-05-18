""""11. Дано список. Вивести спочатку всі негативні елементи,
 а потім всі інші."""


def sorted(list_of_numbers):
    for i in range(len(list_of_numbers)):

        for j in range(i + 1, len(list_of_numbers)):

            if list_of_numbers[i] > list_of_numbers[j]:
                list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]

    return list_of_numbers


list_of_numbers = [-1, 4, 5, -7, -10, -120, -100, 1000, 0, 2000, 84, -292138]
print(*sorted(list_of_numbers))
