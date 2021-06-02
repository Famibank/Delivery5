import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import datareader as web
import pandas_datareader as web
import datetime as dt
import requests

def show_graph():
    # We ask user for the stock ticker and the time frame
    company = input('Put a stock symbol (ex. AAPL, FB, TSLA):  ')
    # start = dt.datetime(input("Put start day-month-year: "))

    date1 = input('Enter the start date in YYYY-MM-DD format: ')
    year, month, day = map(int, date1.split('-'))
    start = dt.datetime(year, month, day)

    date2 = input('Enter the end date in YYYY-MM-DD format: ')
    year, month, day = map(int, date2.split('-'))
    end = dt.datetime(year, month, day)

    data = web.DataReader(company, 'yahoo', start, end)
    
    plt.plot(data['Close'])
    plt.ylabel('f{company} stock price ($)') # fix the name
    plt.show()

