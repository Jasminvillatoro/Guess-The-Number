import random #imports random module

# Welcomes the user and gives information about the game
def display_title():

	print('Welcome to Guess The Number Game')
	print('Guess a number from 1 - 10')

# logic of the game. Let the user know if guess is too high, too low, or correct
def play_game(status):
	 
	random_number = random.randint(1, 10)
	users_guess= 0
	 
	while users_guess != random_number:

		users_guess = int(input('Enter a number from 1 - 10. '))

		if users_guess > random_number:
			print('Too high')

		elif users_guess < random_number:
			print('Too low')

	print('You Guessed It!')
	status = 'no'
	return  status

# Main function for the user to play or exit game
def main():

	display_title()
	play = input('Would you like to play?   Enter YES OR NO. ')

	while play.lower() == 'yes':
		return play_game(play)

	return print('Exiting Game.. Have a good day')

main()