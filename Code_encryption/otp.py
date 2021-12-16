import onetimepad

cipher = onetimepad.encrypt('Приветик от OTP', 'random')
print("Cipher text is ")
print(cipher)
print("Plain text is ")
msg = onetimepad.decrypt(cipher, 'random')

print(msg)