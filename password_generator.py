import random


characters = 'abcdefghijklmnopqrstuvwyxz' \
             'ABCDEFGHIJKLMNOPQRSTUVWYXZ' \
             '1234567890`~-_=+,<.>/?;:{[]}|'

amount_of_passwords = int(input(f'Enter the number of passwords you '
                                f'would like to create: '))
length = int(input("Enter the desired length for your password: "))

for amount in range(amount_of_passwords):
    password = ''
    for chars in range(length):
        password += random.choice(characters)
    print(password)
