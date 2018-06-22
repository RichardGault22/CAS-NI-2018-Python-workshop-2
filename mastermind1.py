#Mastermind game: No duplicates in code
'''
This code will implement the 2 player game Mastermind. To play Mastermind,
the codemaker chooses 4 colours to represent the code. The 6 possible
colours are red,blue,purple,green,yellow or white. ***In this version of
the game the codemaker can use no colour more than once.*** The codemaker
records their 4 colour code in the script below before the code is executed.
The codebreaker will have 10 attempts to guess the code. The codebreaker
must guess both colour and the order correctly. The codebreaker will be
asked to enter their guess for each position. They will be informed
how many colours they guessed correctly and if any colour was in the
correct position.
'''
#1. Codemaker sets up their code: This will be stored in a list
master_code = ['blue','red','green','purple']

#2. Set up codebreaker's guesses:
#Record each guess in a list similar to the master_code
#If we do not know what will be in the list we must fist create
#an empty list where the codebreaker's guess can be stored later
guess = ['','','','']

#2. The codebreaker will be given 10 attempts to guess the code
for attempt in range(10):
    #for each attempt in the list 0,1,2,...,9
    guess[0] = input('What is the first colour?')
    guess[1] = input('What is the second colour?')
    guess[2] = input('What is the third colour?')
    guess[3] = input('What is the fourth colour?')

    #3. Check how many positions were correct
    #Let us keep track of the number of correct positions in a variable
    #'positions_correct'. Initially we have no positions correct.
    positions_correct = 0
    
    #For each colour in the guess, check IF it matches the corresponding
    #colour in the master_code
    for colour in range(4):
        if guess[colour] == master_code[colour]:
            #If it is correct, add 1 to the current total of correct positions
            positions_correct = positions_correct + 1

    #4. Check how many colours were correct
    #Let us keep track of the number of correct colours in a variable
    #'colours_correct'. Initially we have no colours correct.
    colours_correct = 0

    #for each colour in guess
    for colour in range(4):
        #What is the current colour?
        current_colour = guess[colour]
        #check if this colour is located in the mastercode
        if current_colour ==master_code[0]:
            colours_correct = colours_correct+1
        elif current_colour == master_code[1]:
            colours_correct = colours_correct+1
        elif current_colour ==master_code[2]:
            colours_correct = colours_correct+1
        elif current_colour == master_code[3]:
            colours_correct = colours_correct+1

    #5. Tell the codebreaker how the results
    print('You got ',colours_correct,' out of 4 colours correct and ',positions_correct,' in the correct position.')
    #A neater print statement would remove the quotations. To do this the
    #entire print statement must be a long string (use string concatenation,+,
    #and cast integers as strings, str(integer_variable).
    print("You got "+str(colours_correct)+" out of 4 colours correct and "+str(positions_correct)+" in the correct position.")

    #If all four positions were correct, stop the game
    if positions_correct ==4:
        break

#6. To finish the game off tell the codebreaker if they have won or lost
if positions_correct ==4:
    print("Congratulations you won!")
else:
    print("Sorry you ran out of attempts!")
