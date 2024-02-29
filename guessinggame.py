import random

number = random.randint(1, 10)
tries = 0
m_tries = 3

while tries < m_tries:
    guess = int(input("Guess a number between 1 and 10: "))
    tries += 1

    if guess == number:
        print(f"Congratulations! You guessed the correct number in {tries} tries!")
        break
    elif guess < number:
        print("Guess a higher number.")
    else:
        print("Guess a lower number.")

if tries == m_tries:
    print(f"you've reached the maximum number of tries. The number was {number}. Try again next time")

