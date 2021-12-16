import onetimepad

first = onetimepad.encrypt('Hello', '2')
print("1 stage text is ")
print(first)
key1 = "10"
first = first + key1
print("1 Stage + key")
print(first)

second = onetimepad.encrypt(first, '2')
print("2 stage text is ")
print(second)
key2 = "bb"
second = second + key2
print("2 Stage + key")
print(second)

final = onetimepad.encrypt(second, '2')
print("3 stage text is ")
print(final)
key3 = "A"
final = final + key3
print("3 Stage + key")
print(final)

len3 = len(final)
final = final[:len3-1]
second = onetimepad.decrypt(final, '2')

len2 = len(second)
second = second[:len2-2]
first = onetimepad.decrypt(second, '2')

len1 = len(first)
first = first[:len1-2]
msg = onetimepad.decrypt(first, '2')

print("Зашифрованный текст:")
print(msg)