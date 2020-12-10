rus = ' абвгдеёжзиклмнопрстуфхчшщъыьэюя'
n = input('Введите сообщение для кодировки:')
key = int(input('Пожалуйста введите ключ: 1 - 33:'))
n = n.lower()
encrypted = ""
for letter in n:
    position = rus.find(letter)
    newPosition = position + key
    if letter in rus:
        encrypted = encrypted + rus[newPosition]
    else:
        encrypted = encrypted + letter
print("Твоё слово:", encrypted)