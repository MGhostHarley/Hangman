This project was started to get practice with 3 things:

1. Reading in a file

I wanted practice on how read in a file and then manipulate it. In this project, I read in a dictionary of words and store it in a list that can then be used later.

2. List manipulation

I also wanted to be able to manipulate and print out lists. In this project there are four main lists: one that stores a list of words (dictionary_list), one that contains each letter in the randomly chosen (guessing_word), a list that is displayed that has the blanks spaces of the picked word and is slowly filled out by the correct letter guesses (right_guessed_letter) and a list that keeps track of all the guessed letters (already_guessed). 

This project focuses on comparing lists together, and manipulating them based on results found; for example if the user guesses a letter in the guessing_word list, the right_guessed_letter list must be updated with the letter at the correct index and printed out. The letter must also be added to the already_guessed list to prevent duplicate guesses

3. Input Validation

THis was the funnest and trickiest part of the project - thinking of ways to break the software. Sanitizing the information so that it was only letters taught me a lot about built in python methods and paremeter checking.


As I was testing the program, I noticed that the words could be quite difficult to pick; so I decided to create levels that determined the difficulty with 1 being easy, 2 being meduim and 3 being hard. I initially found checking if the input was an integer to be difficult so I ended up using Try/Except combined with conditional checks to be do this.

A. Possible future features

The next two features planned for this project is allowing the user to pick their own word and checking to make sure its a real word to play with a friend and implimenting a gui element. I believe the first additional feature mentioned shouldn't be too difficult, but I will need to research more on python gui libraries.

B Community Help:

Please feel free to download and test and suggest changes and anything that can be optimized. 



-M. Harley

