import random #imports random module

# Project Guess The Number 
# program will have functions 
# first to display title and program specifications
# second - plays the game
# third main function calls those functions and controls the game

def display_title():
	print('Welcome to guess a number')
	play = input('Would you like to play?   Enter YES OR NO. ')
	print(play)

	return play

def play_game():

	random_number = random.randint(1, 10)
	print(random_number)
	users_guess= 0
	 
	while users_guess != random_number:

		users_guess = int(input('Enter a number from 1 - 10. '))
		print('users guess is', users_guess)

		if users_guess > random_number:
			print('Too high')

		elif users_guess < random_number:
			print('Too low')

	print('You guessed it!')
	main()
 

def main():
	play = display_title()
	while play == 'yes':
		play_game()
	return print('Have a good day')


main()