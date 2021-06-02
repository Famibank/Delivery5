# c2qi8uiad3ickc1lnvu0 - the API Key for Apple stock from finnhub.io - found it just by googling, looks legit
import requests
from Account import Account
from stocks import show_graph

is_logged_in = False
while is_logged_in == False:
    answer = input('Press 1 to login\nPress 2 to register\n')
    if answer == '1':
        if Account().login():

            is_logged_in = True
            while is_logged_in == True:
                a = input('Would you like to see the stock price of a particular company (through the Yahoo Finanace API connection)?\nPress 1 to see.\nPress 2 to stop app.\n')

                if a == "1":
                    show_graph()
                elif a == '2':
                    break
                #make it so it doesnt stop program.

        else: print("Incorrect, please try again.")
    elif answer == '2':
        Account().register()
    else:
        print('Input not recognized')
