"""A collection of function for doing my project."""

import random
import string


def set_target_number(mini, maxi):
    """Randomly select an integer between a minimum integer and a maximum integer.
    
    Parameters
    ----------
    mini : int
        The lower bound of a range.
    maxi : int
        The upper bound of a range.
        
    Returns
    -------
    ramdom_number : int
        The random integer between the lower bound and the upper bound.
    """  
    ramdom_number = random.randint(mini, maxi) 
    return ramdom_number


def quit_game(player_input):
    """End the guess game once the player inputs a certain sting.
    
    Parameters
    ----------
    player_input : str
        The player's input.
    
    Return
    ------
    bool
        Check if the player quit the game.
    """
    if 'quit game' in player_input:     
        return True
    
    else:
        return False
    
    
def check_min():
    """Check if player's input of minimum is an integer.
    
    Returns
    ------
    typemin: bool
        Check if the player's input of minimum is an integer.
    min1 : str
        Import the player's input.
    minimum : int
        The integer form of the player's valid input.
    """
    typemin = False
    while True:
        
        minimum = None
        min1 = input('Minimum :\t')
        
        if min1.isdigit():
            
            minimum = int(min1)
            typemin = True
            
            # End the loop once the player inputs an integer.
            break
            
        elif quit_game(min1):
            
            print('=========You leave the game=========')
            print("Type 'guess' to play again.")
            
            # End the game when the player choose to leave the game.
            break
            
        # Prompt the player to type a valid minimum        
        else:
            
            print("Oops! That was not a valid minimum. "+'\n'+
                  "Please type a non-negative integer ",\
                  "or type 'quit game' to leave the game.")
            
    return typemin, min1, minimum



def check_max():
    """Check if player's input of minimum is an integer.
    
    Returns
    ------
    typemin: bool
        Check if the player's input of minimum is an integer.
    min1 : str
        Import the player's input.
    minimum : int
        The integer form of the player's valid input.
    typemax: bool
        Check if the player's input of maximum is an integer.
    max1 : str
        Import the player's input.
    maximum : int
        The integer form of the player's valid input.
    """
    typemin, min1, minimum = check_min()
    typemax = False
    while True:
        
        maximum=None
        max1= None
        
        if typemin == True:
            
            max1 = input('Maximum :\t')
            
            if max1.isdigit() and int(max1) > minimum:
                
                maximum = int(max1)   
                typemax = True
                
                # End the loop once the player inputs an integer.
                break
                
            # Prompt the player to type a valid maximum    
            elif max1.isdigit() and int(max1) <= minimum:

                print("Oops! That was not a valid maximum. "+'\n'+
                      "Please make sure the maximum > the minimum." +'\n'+
                      "To leave the game, type 'quit game'.")
                
            elif quit_game(max1):

                print('=========You leave the game=========')
                print("Type 'guess' to play again.")
                break
                
            else:

                print('Oops! That was not a valid maximum.' + '\n' +
                      "Please type a non-negative integer ",\
                      "or type 'quit game' to leave the game.")
                
        # The while loop breaks if the player left the game when inputing minimum.
        else:
            break

    return typemin, min1, minimum, typemax, max1, maximum
    
    
def guessing_game():
    """Function used to play the number guessing game.
    
    """            
    print('===========Guessing Game!===========')     
    print('The Number Guessing Game will begin, hope you enjoy it!', '\n',
          'Remember you can quit the game anytime',
          "by typing 'quit game'!", '\n',
          'Please set a range first.')
    
    typemin, min1, minimum, typemax, max1, maximum = check_max()  
    not_quit_game = True
    
    # If the player inputs valid minimum and maximum,
    # generate the target number based on the player's input
    if typemin == True and typemax == True:    
        
        target_number = set_target_number(minimum, maximum)
        print('Your customized range is ', minimum, ' - ', maximum, '.')
        
    else:
        
        not_quit_game = False
        
    count = 0    
    while not_quit_game:
        
        player_text = input('Your guess:\t')
        
        if player_text.isdigit():
            
            guess_number = int(player_text)
            
            # Count number of attempts the player has.
            count += 1
            print('Number of attempts: ', count)
            
            if guess_number > target_number:
            
                print("Guess a smaller number.")
            
            elif guess_number < target_number:
            
                print("Guess a bigger number.")

            elif guess_number == target_number:
            
                print('Congratulation! The answer is: ', guess_number)
                print('Your number of attempt is: ', count)
                print("===Game ends, type 'guess' to try again :)===")
                not_quit_game = False
                
        elif (player_text.isdigit() == False) and(not quit_game(player_text)):
            
            print("Sorry, please type an integer," \
                  "or type 'quit game' to leave the game.")

        elif quit_game(player_text):
            
            print('=========You leave the game=========')
            print("Type 'guess' to play again.")
            not_quit_game = False
            
    
# Codes below are got from homework 3

# Check if the input is a question
def is_question(input_string):
    
    if '?' in input_string:
    
        return True
    
    else:
        
        return False
    
    
# get rid of all punctuation
def remove_punctuation(input_string):
    
    out_string = ''
    
    for x in input_string:
        
        if x not in string.punctuation:
            
            out_string += x
            
    return out_string


# Prepare the text inputs for processing.
def prepare_text(input_string):
    
    temp_string = input_string.lower();
    temp_string = remove_punctuation(temp_string)
    
    out_list = temp_string.split(" ")
    
    return out_list


# Return a string that has been repeated a specified number of times
# With a given separator
def respond_echo(input_string, number_of_echoes, spacer):
    
    if input_string is not None:
        
        echo_temp = input_string+spacer
        echo_output = echo_temp*number_of_echoes
        
    else:
        
        echo_output = None
        
    return echo_output


# Select an output for the chatbot, based on the input it got
def selector(input_list, check_list, return_list):
    
    output = None
    
    for x in input_list:
        
        if x in check_list:
            
            output = random.choice(return_list)
            
            break
            
    return output


# Concatenate two strings
# Combining them with a specified separator.
def string_concatenator(string1, string2, separator):
    
    if string1 == None or string2 == None or separator == None:
        
        output = None
        
    else:
        
        output = string1 + separator + string2
        
    return output


def list_to_string(input_list, separator):
    
    output  = input_list[0]
    
    for i in range(1, len(input_list)):
        
        output = string_concatenator(output, input_list[i], separator)
        
    return output


def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""   
    for element in list_one:
        
        if element in list_two:
            
            return element
        
    return None


def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""  
    for element in list_one:
        
        if element in list_two:
            
            return True
        
    return False


# End the chat
def end_chat(input_list):
    
    if 'quit' in input_list:
        
        return True
    
    else:
        
        return False

    
# start chat
def have_a_chat():
    """Main function to run our chatbot."""
    GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
    GREETINGS_OUT = ["Hello, it's nice to talk to you!", 'Nice to meet you!',  "Hey - Let's chat!"]

    COMP_IN = ['python', 'code', 'computer', 'algorithm', 'language']
    COMP_OUT = ["Python is what I'm made of.", \
                "Did you know I'm made of code!?", \
                "Computers are so magical", \
                "Do you think I'll pass the Turing test?"]

    PEOPLE_IN = ['turing', 'hopper', 'neumann', 'lovelace']
    PEOPLE_OUT = ['was awesome!', 'did so many important things!', 'is someone you should look up :).']
    PEOPLE_NAMES = {'turing': 'Alan', 'hopper': 'Grace', 'neumann': 'John von', 'lovelace': 'Ada'}

    JOKES_IN = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol']
    JOKES_OUT = ['ha', 'haha', 'lol'] 

    NONO_IN = ['matlab', 'java', 'C++']
    NONO_OUT = ["I'm sorry, I don't want to talk about"]

    UNKNOWN = ['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!']
    QUESTION = "I'm too shy to answer questions. What do you want to talk about?"
    
    # Detect if the user want to play the number guessing game.
    GUESS = ['guess']
 
    chat = True
    print('Hello, this is Alva, a happy chatbot! ', '\n'
          "You can play the number guessing game by typing 'guess' ",\
          'or just chat with me! ', '\n'
          "To quit, please type 'quit'.")
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        # Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))

            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, COMP_IN, COMP_OUT))

            # Check if the input mentions a person that is specified, add a person output if so
            if is_in_list(msg, PEOPLE_IN):
                
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name], name.capitalize(),
                                            selector(msg, PEOPLE_IN, PEOPLE_OUT)], ' '))

            # Check if the input looks like a joke, add a repeat joke output if so
            outs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))

            # Check if the input has some words we don't want to talk about, say that, if so
            if is_in_list(msg, NONO_IN):
                
                outs.append(list_to_string([selector(msg, NONO_IN, NONO_OUT), find_in_list(msg, NONO_IN)], ' '))

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)

        # Start the number guessing game
        if(is_in_list(msg, GUESS)):
     
            guessing_game()
