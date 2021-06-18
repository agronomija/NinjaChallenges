import random
import json
import datetime

with open('score_list.json', 'r') as score_file:
    score_list = json.loads(score_file.read())
    print(score_list)

secret = random.randint(1, 30)
attempts = 0
unsuccesful_guesses = 0





while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        score_list.append({'attempts': attempts, 'date': f'{datetime.datetime.now()}', 'false_attempts': unsuccesful_guesses})
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        unsuccesful_guesses += 1
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
        unsuccesful_guesses += 1

sorted_by_attempts = []

with open('score_list.json', 'w') as score_file:
    score_file.write(json.dumps(score_list))