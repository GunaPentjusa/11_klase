import random
import datetime

computer_number = random.randint(1, 100)
continue_game = True
user_guesses = []
start_time = datetime.datetime.now()

def calculate_average_difference():
    sum_of_differences = 0
    for n in user_guesses:
        sum_of_differences += abs(n - computer_number)

    return sum_of_differences/len(user_guesses)

while(continue_game):
    user_guess = int(input('Uzmini skaitli starp 1 un 100: '))
    user_guesses.append(user_guess)

    if user_guess == computer_number:
        print('Precīzi, tu uzminēji!')
        continue_game = False
    elif user_guess < computer_number:
        print('Vairāk')
    elif user_guess > computer_number:
        print('Mazāk')
    else:
        print('Notika kļūda!')

print('Game over!')

print(f'Vidēja starpība bija {calculate_average_difference()}')
print(f'Tu spēlēji {datetime.datetime.now()-start_time} sekundes')
