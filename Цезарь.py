rus = ' ������������������������������'
n = input('������� ��������� ��� ���������:')
key = int(input('���������� ������� ����: 1 - 33:'))
n = n.lower()
encrypted = ""
for letter in n:
    position = rus.find(letter)
    newPosition = position + key
    if letter in rus:
        encrypted = encrypted + rus[newPosition]
    else:
        encrypted = encrypted + letter
print("��� �����:", encrypted)