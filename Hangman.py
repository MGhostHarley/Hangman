import math 
import random
import os
import sys

#os.path.abspath("Hangman/dictionary.txt")

def dictionary_list():

	with open('dictionary.txt', 'r') as file: 						#reads in  file
		dict_list = file.read().replace('/n', ' ') 					# replaces every new line with a space
	words = dict_list.split()										#creates a list by splitting at spaces
	return words

def pick_random_word(some_list):

	secure_random = random.SystemRandom() 							#creates an object with the secure method of random
	return secure_random.choice(some_list) 							#returns a random choice from some list


	

 


def main():

	counter = 6 													# keeps track of guesses
	right_guessed_letter = []										# where we show correctly guessed letters
	already_letter = [] 											# where we show letters
	guessing_word = list(pick_random_word(dictionary_list()))		# picks a rondom word from my dictionary  and makes a list of characters



	


	while True:																								#Keeps going until I have a valid integer input
		try:																								#Want to try to see if input is an integer and catch exception if not; Implementing difficulty levels
			difficulty = int(raw_input('Chose a dificulty: \n 1 for easy \n 2 for medium \n 3 for hard'))   #converts sting number into int number
			if difficulty < 1 or difficulty >3:																#has to be between 1,2,3 for easy, medium or hard levels
				print '\n Please pick 1, 2, or 3 and no other number'
			elif difficulty == 1:
				while True:																					#This whole elif statement says that if input is 1, keep picking a word until it is 4 letters or less
					if len(guessing_word) > 4:
						guessing_word = list(pick_random_word(dictionary_list()))
					else:
						break
				break 																						#Breaks out of outer loop because we have word of length we want. Repeated in other if statements
			elif difficulty == 2:
				while True:																					#This whole elif statement says that if input is 2, keep picking a word until it is b/w 5 and 7
					if len(guessing_word) > 7 or len(guessing_word) < 5:
						guessing_word = list(pick_random_word(dictionary_list()))
					else:
						break
				break
			elif difficulty == 3:
				while True:																					#This whole elif statement says that if input is, keep picking a word until it is greater than 7 letters
					if len(guessing_word) <7:
						guessing_word = list(pick_random_word(dictionary_list()))
					else:
						break
				break
		
			else: 
				break
		except ValueError:
			print("\n That's not an integer! Try again")													#This catches the value error of a non integer and runs it again
		continue

		

		

	for length_of_word in guessing_word: 							#for the lenght of my word
		right_guessed_letter.append('_ ') 							#create a list of blank spaces
	
	print right_guessed_letter 										# shows it



	while counter > 0:
		letter = raw_input("Guess a letter: " ).lower() 					#read in imput and makes sure its all lowercase

		if letter.isalpha() == False: 											#of the input is not a letter make them try again
			print 'You have to enter a letter. Try again. '
		elif  len(letter)>1: 													#if they enter multiple letters, make themn try again
			print 'Enter one letter at a time. Try again. '
		elif letter in already_letter: 											#if they have already guessed the letter, make them try again
			print "You already guessed: %s Try again. " % already_letter
		elif letter in guessing_word: 											#:if the letter they guessed is in the actual word:
			for this_letter_index in xrange(0, len(guessing_word)): 				#iterate through the guessed word ...
				if guessing_word[this_letter_index] == letter: 						#each time the guessed letter is equal to the letter in the actual word ...
					right_guessed_letter[this_letter_index] = letter 				#replace the dash in the blankspace list with that letter
					already_letter.append(letter)
			print right_guessed_letter											#print the new blank space list for the user to see
		
		else: 
			counter -=1                                                             #decrement counter to decrease turn count
			if letter not in already_letter:                                        #This line makes sure we aren't adding letters already in the list
				already_letter.append(letter) 										#add any guessed letter to already guessed letter list

			if counter == 0:													#if the counter hits zero, game over and print out the joined word
				print "You lose. The word was %s" % ''.join(guessing_word)
			else:
				print "Wrong. You have %d tries. Try again" % counter			#Prints out the number of tries
				print " \nThese are the letters you have guessed: \n" + ', '.join(already_letter) + '\n' 			#prints out a running total of letters guesses (stored in already letter) and formatted nicely
	
		
		if guessing_word == right_guessed_letter:								#Checks win condition and then breaks out of while loop if met
			print "You Win! The word was %s" % ''.join(guessing_word)
			break



	
main()





