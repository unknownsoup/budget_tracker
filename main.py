import csv
import mysql.connector
import pandas as pd

def get_database_connection():
    return mysql.connector.connect(host='localhost', user='root', passwd='braedon123', database='budgettracker')

connection = get_database_connection()
cursor = connection.cursor()

def add_deposit():
    amount = float(input("Deposit Amount($): "))
    sql = "INSERT INTO deposits (amount, date)"

def main():
    while True:
        print("\n1. Check Balance\n2. Add an Expense\n3. Add a deposit\n4. View Account History\n5. Exit")
        option = input("Choose an option: ")
        if option == '1':
            pass
        if option == '2':
            pass
        if option == '3':
            add_deposit()
        if option == '4':
            pass
        elif option == '5':
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
   main()