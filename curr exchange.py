from locale import currency
from random import random
from time import time
from unittest import result
from requests import get
from pprint import PrettyPrinter
import time
from wikipedia import *
import random
import mysql.connector
import datetime

BASE_URL = "https://free.currconv.com/"
API_KEY = "562ddaf40c95f5d58108"

printer = PrettyPrinter()

def databaseinsert(currency1,currency2,amount,uid,converted_amount):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="imamdb")

    x=datetime.datetime.now()
    mycursor = mydb.cursor()

    mycursor.execute('INSERT INTO currencyconvert(uid,basecurrency,convertcurrency,baseamount,convertedamount,datetime) VALUES(%s,%s,%s,%s,%s,%s)',(uid,currency1,currency2,amount,converted_amount,x))
    mydb.commit()





def currInfo(currencyinfo):
    print("\n")
    print(summary(currencyinfo+" currency",sentences=3))
"""result = wikipedia.search(str(currencyinfo)+" currency")
    for search in result:
        print(search)
        print(wikipedia.page(search).summary)"""

def exchangeWithdrawal(currency1,currency2,amount,uid,converted_amount):
    print("Processing.....")
    time.sleep(3)
    print("Please collect your:",str(converted_amount),currency2)
    databaseinsert(currency1,currency2,amount,uid,converted_amount)
    

def exchangeDeposit(currency1,currency2,amount,uid,converted_amount):
    amount=int(amount)
    print("Please deposit",str(amount),currency1)
    time.sleep(2)
    attempts=3
    while attempts>0:
        dep=int(input("Enter the amount for confirmation:"))
        if dep==amount:
            time.sleep(2)
            print("Deposit succesfull!")
            exchangeWithdrawal(currency1,currency2,amount,uid,converted_amount)
            break
        else:
            time.sleep(2)
            print("Not the correct amount")
            attempts-=1
            print("Attempts left:",str(attempts))


        


def exchangeCurrencies(currency1,currency2,amount,uid,converted_amount):
    uid=int(uid)
    print("WELCOME TO THE URBAN EXCHANGE!")
    attempts=3
    while attempts>0:
        user_uid=int(input("Please enter the unique id for your requested exchange:"))
        time.sleep(3)
        if user_uid == uid:
             print("UID verification successfull")
             time.sleep(2)
             print("Your request is for",str(amount),currency1,'to',currency2)
             exchangeDeposit(currency1,currency2,amount,uid,converted_amount)
             break
             
        else:
             print("Wrong UID")
             attempts-=1
             print("You have",str(attempts),"attempts left!")


    



def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())
    data.sort()

    return data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")


def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print('Invalid currencies.')
        return

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")

    exc=input("Do you want to Exchange the above currencies?(yes/no)\n").lower()
    if exc=='yes':
        uid=random.randrange(1000000,2000001)
        print("Your uniqueID for the exchange is:",uid)    
        print('Redirecting too exchange....')
        time.sleep(2)
        exchangeCurrencies(currency1,currency2,amount,uid,converted_amount)
    elif exc=='no':
        print("Okay!")
    else: 
        print("Invalid Option!")
        
    return converted_amount


def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Rate - get the exchange rate of two currencies")
    print("Convert - convert from one currency to another")
    print("Info - get the information about the currency ")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        elif command =="info":
            print("NOTE:Please enter full name of the currency to avoid contradiction use list option if you want to and then find the info.")
            currencyinfo = input("Enter the currency you want the info about:").upper()
            currInfo(currencyinfo)
        else:
            print("Unrecognized command!")

main()