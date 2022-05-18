spisok = []
spisok_yes = []
spisok_no = []
while True:
    digit = int(input())
    if digit == 0:
        break
    else:
        spisok.append(digit)
for i in spisok:
    if i%2 == 0:
        spisok_yes.append(i)
    else:
        spisok_no.append(i)
print('Парнs:', spisok_yes)
print('Непарні:', spisok_no)
