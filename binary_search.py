import random
secret = random.randint(1, 101)

while True:
  
  guess = int(input("Guess a number between 1 and 100: "))
  
  if guess > secret:
    print("Too high.")
  elif guess < secret:
    print("Too low.")
  else:
    print("You got it.")
    break
