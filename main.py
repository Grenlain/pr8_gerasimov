import random

 HEAD
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ1234567890'
chars = '+-/*!&$#&=@<>abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
 dev
number = input('Количество паролей?'+"\n"
length = input('длина паролей?'+"\n"
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(lenght):
        password += random.choice(chars)
    print(password)

