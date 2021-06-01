# c2qi8uiad3ickc1lnvu0 - the API Key for Apple stock from finnhub.io - found it just by googling, looks legit
import requests
import database
from class_example import Person

user_name_value = "69696969"
password_value = "123"


is_logged_in = False
while is_logged_in == False:
    user_name = input("What's your CPR?\n")
    password = input("Type in your password:\n")
    if user_name == user_name_value and password == password_value:

            is_logged_in = True

            a = input('Would you like to see the current Apple stock price? \n Press 1 to see. \n Press 2 to go Back. \n')

            if a == "1":
                r = requests.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=c2qi8uiad3ickc1lnvu0')
                print("Current stock price", r.json()['c'])
#if a == "2": ---this for later to go Back
    else: print("Incorrect password and/or CPR, please try again. ")

#database.Hi()
Person().greet() #first is class, then function
"""
Sample response
1
2
3
4
5
6
7
8
{
  "c": 261.74,
  "h": 263.31,
  "l": 260.68,
  "o": 261.07,
  "pc": 259.45,
  "t": 1582641000
}
Toms sent Šodien plkst. 20:06

Response Attributes:

o
Open price of the day

h
High price of the day

l
Low price of the day

c
Current price

pc
Previous close price
"""
