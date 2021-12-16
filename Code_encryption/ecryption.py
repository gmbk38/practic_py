from collections import Counter


def encrypt(k, m): 
    set_ords = [(x + k) % 65536 for x in map(ord, m)]
    return ''.join(map(chr, set_ords))


def decrypt(k, m):  
    set_ords = [(x - k) % 65536 for x in map(ord, m)]
    return ''.join(map(chr, set_ords))


def hack(m): 
    most_common = Counter(m).most_common()[0][0]
    key = ord(most_common) - ord(' ')
    return decrypt(key, m)


key = int(input('Введите ключ: '))
text = encrypt(key, "Смогу ли я переступить или не смогу! Осмелюсь ли нагнуться и взять или нет? Тварь ли я дрожащая или право имею… ")
print('Зашифрованный текст: ', text)
print('Расшифрованный текст:  ', decrypt(key, text))
print('Взломанный текст: ', hack(text))
