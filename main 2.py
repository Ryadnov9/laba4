""""7.Дано рядок. Розріжте його на дві рівні частини
(якщо довжина рядка - парна, а якщо довжина рядка непарна,
то довжина першої частини повинна бути на один символ більше).
Переставте ці дві частини місцями, результат запишіть в новий рядок
і виведіть на екран."""

word = input("Слово: ")
half1 = word[:int((len(word)+1)/2)]
half2 = word[int((len(word)+1)/2):]
print(half2 + half1)
