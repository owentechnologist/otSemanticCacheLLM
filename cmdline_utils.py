# This is a collection of 
# 1. cmdline UI code

# This string is used to separate areas of command line output: 
spacer = "\n**********************************************"

## this function displays the commandline menu to the user
## it offers the ability to end the program by typing 'end'
def display_menu():
    print(spacer)
    print('\tType: END   and hit enter to exit the program...\n')
    print('\tCommandline Instructions: \nType in your prompt/question as a single statement with no return characters... ')
    print('(only hit enter for the purpose of submitting your question)')
    print(spacer)
    # get user input/prompt/question:
    user_text = input('\n\tWhat is your question? (prompt):\t')
    if user_text =="END" or user_text =="end":
        print('\nYOU ENTERED --> \"END\" <-- QUITTING PROGRAM!!')
        exit(0)
    return (user_text)

# bootstrap value, as we later check for the existence of user_input
user_input = "BEGIN"
