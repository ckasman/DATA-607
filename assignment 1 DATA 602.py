#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:11:37 2018

@author: christinakasman
"""
#import numpy and pandas
import numpy as np
from pandas import *
import pandas as pd

#Cash
start_cash= 100000000

import time;

#timestamp
localtime = time.asctime( time.localtime(time.time()) )

#main menu to choose options
def print_menu():
    print('1. Trade')
    print('2. Show Blotter')
    print('3. Show P/L')
    print('4. Quit')
#Trade menu listing 5 equities   
def trademenu():
    print("1. Apple")
    print("2. Amazon")
    print("3. INTC")
    print("4. Microsoft")
    print("5. SNAP")
    print("6. quit")
#would you like to proceed with trade menu
def print_proceed():
    print("1. Yes")
    print("2. No")
    #Buy/ Sell menu
def print_buysell():
    print('1. Buy')
    print('2. Sell')
    
#scraping equity prices off of Yahoo Finance
import bs4 as bs
import urllib.request 

def get_quote(symbol):
    url = urllib.request.urlopen('https://finance.yahoo.com/quote/' + symbol)
    soup=bs.BeautifulSoup(url,'html.parser')
    contain = soup.find('span', attrs={'class':'Trsdu(0.3s)'})
    contain = contain.text
    print(contain)
    
#blotter
blotter = pd.DataFrame({
        'Side': [], 
        'Ticker': [],
        'Quantity': [], 
        'Executed Price':[], 
        'Execution Timestamp':[], 
        'Money In/ Money Out':[]
})

#PL
PL = {'Ticker': [], 'Position': [],'Market':[], 'WAP':[], 'UPL':[], 'RPL':[]}
dfpl = pd.DataFrame(data=PL)



#Program
done = False
while not done:
    print_menu()
    selected = input("Enter your selection[1-4]: ")
    if selected == '4':
        done = True
#Trade menu
    elif selected == '1':
        while not done:
            trademenu ()
            selected = input("\nEnter your selection[1-6]: \n") #Choose equity
            if selected == '1': #Apple
                price = get_quote("AAPL")
                x = int(input('select quantity to be traded: \n'))
                print_proceed()
                choice = input('Confirm trade?[Y/N]: \n') #Confirm Trade
                if choice == '1':
                    print_buysell() #Menu to buy or sell
                    option = input('Buy or Sell?: ')
                    if option == '1': #Buy 
                        blotter.insert('Buy', 'AAPL', print(x), print(y), localtime, "price") #xy
                    elif option == '2': #Sell
                        blotter.insert('sell', 'AAPL', x, y, localtime) #xy)
                elif choice == "2": #Do not confirm
                    done = True
            elif selected == '2':
                y = get_quote("AMZB")
                x = int(input('select quantity to be traded: '))  #show amou1nt
                print_proceed()
                choice = input('Confirm trade?[Y/N]: ') #Confirm Trade
                if choice == '1':
                    print_buysell() #Menu to buy or sell
                    choice = input('Buy or Sell?: ')
                    if choice == '1': #Buy 
                        blotter.insert('buy', 'AMZN', x, y, localtime, x*y) #xy)
                    elif choice == '2': #Sell
                        blotter.insert('sell', 'AMZN', x, y, localtime) #xy)
                elif choice == "2": #Do not confirm
                    done = True
            elif selected == '3':
                y = get_quote("INTC")
                x = int(input('select quantity to be traded: '))  #show amount
                print_proceed()
                choice = input('Confirm trade?[Y/N]: ') #Confirm Trade
                if choice == '1':
                    print_buysell() #Menu to buy or sell
                    choice = input('Buy or Sell?: ')
                    if choice == '1': #Buy 
                        blotter.insert('buy', 'INTC', x, y,localtime) #xy)
                    elif choice == '2': #Sell
                        blotter.insert('sell', 'INTC', x, y, localtime) #xy)
                elif choice == "2": #Do not confirm
                    done = True
            elif selected == '4':
                y = get_quote("MSFT")
                x = int(input('select quantity to be traded: '))  #show amount
                print_proceed()
                choice = input('Confirm trade?[Y/N]: ') #Confirm Trade
                if choice == '1':
                    print_buysell() #Menu to buy or sell
                    choice = input('Buy or Sell?: ')
                    if choice == '1': #Buy 
                        blotter.insert('buy', 'MSFT', x, y, localtime) #xy)
                    elif choice == '2': #Sell
                        blotter.insert('sell', 'MSFT', x, y, localtime) #xy)
                elif choice == "2": #Do not confirm
                    done = True
            elif selected == '5':
                y = get_quote("SNAP")
                x = int(input('select quantity to be traded: '))  #show amount
                print_proceed()
                choice = input('Confirm trade?[Y/N]: ') #Confirm Trade
                if choice == '1':
                    print_buysell() #Menu to buy or sell
                    choice = input('Buy or Sell?: ')
                    if choice == '1': #Buy 
                        blotter.insert('buy', 'SNAP', x, y, localtime) #xy)
                    elif choice == '2': #Sell
                        blotter.insert('sell', 'SNAP', x, y, localtime) #xy)
                elif choice == "2": #Do not confirm
                    done = True
            elif selected =='6':
                done = True
    elif selected == "2":
        print(blotter)
    elif selected == "3":
        print(dfpl)
    else:
        print('Invalid Choice. Please enter 1-4')
        print_menu()
        
        
