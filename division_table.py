user_input = int(input('Enter the number you\'d like a division table for. \n'))

for _ in range(1, user_input + 1):
    print(user_input, '/', _, '=', user_input / _)
