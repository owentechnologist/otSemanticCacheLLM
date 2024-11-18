# This is a collection of 
# 1. cmdline UI code
# 2. Redis connection establishment code

import sys,getopt,redis


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

### Redis Setup / functions: ###

## checks sys.args for host and port etc...
## the following values are placeholders 
redis_host = 'USER-PROVIDED'#'redis-10000.re-cluster1.ps-redislabs.org'
redis_port = 10000
redis_password = ""
redis_user = "default"

# skip the name of this script, and look at the args that follow:
argv = sys.argv[1:] 
opts,args = getopt.getopt(argv,"h:p:s:u:", 
                                ["host =",
                                "port =",
                                "password =",
                                "username =",
                                ]) 
for opt,arg in opts:
    if opt in ['-h','-host']:
        redis_host = arg
    elif opt in ['-p','-port']:
        redis_port = arg
    elif opt in ['-s','-secret_password']:
        redis_password = arg
    elif opt in ['-u','-username']:
        redis_user = arg
if len(sys.argv)<4:
    print('\nPlease supply a hostname & port for your target Redis instance:\n')
    print('\n\tYour options are: host port password username:')
    print('-h <host> -p <port> -s <password> -u <username>')
    exit(0)

# check for Redis password & need for simple authentication:
if redis_password == "" and redis_user == "default":
    redis_connection = redis.Redis( host=redis_host, port=redis_port, encoding='utf-8', decode_responses=True)
else:
    redis_connection = redis.Redis( host=redis_host, port=redis_port, password=redis_password ,username=redis_user, encoding='utf-8', decode_responses=True)

