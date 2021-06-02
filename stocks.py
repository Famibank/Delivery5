import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import requests

def show_graph():
    # We ask the user for the stock symbol and the dataframe he/she is interested in.
    company = input('Put a stock symbol (ex. AAPL, FB, TSLA):  ')

    date1 = str(input('Enter the start date in YYYY-MM-DD format: '))
    year, month, day = map(int, date1.split('-'))
    start = dt.datetime(year, month, day)

    date2 = str(input('Enter the end date in YYYY-MM-DD format: '))
    year, month, day = map(int, date2.split('-'))
    end = dt.datetime(year, month, day)

    data = web.DataReader(company, 'yahoo', start, end) # We download the data from Yahoo Finance API

    plt.plot(data['Close']) #Starts the plot with the closing price of each day for the selected time period.
    plt.ylabel(f'{company} Stock price ($)') #Names the y axis according to which stock was chosen.
    plt.xlabel('Date (YYYY,MM,DD)') #Name of the x axis.
    plt.xticks(rotation=70, ha='right') #Rotates the ticks on the x axis for better view
    plt.show() #Displays the plot.
