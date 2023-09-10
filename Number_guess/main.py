import random

k = random.randrange(0,100)
print('THIS IS A NUMBER GUESSING GAME. YOU HAVE THE NUMBER AND YOU HAVE 10 TRIES')
tri = 9

for i in range(11):
    try:
        num = int(input('Enter the guessing number: '))
    except ValueError:
        print('Please enter a valid integer.')
        continue

    if num>k:
        print('The number you guessed is greater than the estimated number.')
    elif num<k:
        print('The number you guessed is smaller than the estimated number.')
    elif num==k:
        print('You guessed it right, the actual number is ', k)
        print('You took' , 10-tri , 'attempts to guess the number.')
        break
    tri = tri - 1
    print('You have ' , tri , ' tries left.')
