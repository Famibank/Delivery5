import requests
from Account import Account
from stocks import show_graph

is_logged_in = False #Defines variable that will be used later.
while is_logged_in == False: #Sets the app so that the user cannot access the bank account before logging in.
    answer = input('Press 1 to login\nPress 2 to register\n')
    if answer == '1':
        if Account().login(): #Calls the login function from Account class and checks the function output (True or False).

            is_logged_in = True #If function output is True then assigns is_logged_in variable to True.
            while is_logged_in == True: #Creates a while loop.

                a = input('Would you like to see the stock price of a particular company (through the Yahoo Finanace API connection)?\nPress 1 to see.\nPress 2 to stop app.\n')

                if a == "1": #If user inputs 1, it initiates the show_graph function.
                    show_graph() #Calls for the function.
                elif a == '2': #If user inputs 2, it stops the program.
                    break

        else: print("Incorrect, please try again.") #If login function returns False, asks user to try again.
    elif answer == '2': #If user inputs 2 - the registration begins.
        Account().register()
    else:
        print('Input not recognized') #If user inputs anything else but 1 and 2.
