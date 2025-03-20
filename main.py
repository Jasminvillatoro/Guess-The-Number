"""Module providing the randint method """
import random 
# Welcomes the user and gives information about the game
def display_title():
	print('Welcome to Guess The Number Game')
	print('Guess a number from 1 - 10')

# Logic of the game. Lets the user know if guess is too high, too low, or correct
# In this function we use the randint() method which returns a random number from 1 - 10
def play_game():
		random_number = random.randint(1, 10)
		user_guess = 0

		while user_guess != random_number:
			user_guess = int(input('Enter a number from 1 - 10. '))

			if user_guess > random_number:
				print('Too high')

			elif user_guess < random_number:
				print('Too low')

		print('You Guessed It!')
		# Once, returned user will get prompted to play the game again or not.
		return  main()

# Main function
# Prompts the user to play the random number game or to exit 
def main():
	display_title()
	user_play = input('Would you like to play?   Enter YES OR NO. ')
	# While loop. if the user enters yes the play game function will be called.
	# User enters no the last statement will run.
	while user_play.lower() == 'yes':
		return play_game()

	return print('Exiting Game.. Have a good day')

main()