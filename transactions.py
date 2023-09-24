"""
5-minute automation for transactions.

Preferred method: CRON Job
WHILE loop may drift time

Installation:
pip install pandas
"""

import os.path

from csv import writer
import pandas as pd

from datetime import datetime
import time
from random import randrange


def make_a_transaction(transaction_id):
    transactionId = transaction_id
    productId = randrange(10,50,10)
    transactionAmount = randrange(1000,5000,1000)
    transactionDatetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    transaction_list = [transactionId, productId, transactionAmount, transactionDatetime]
    
    return transaction_list

path = 'data/Transaction_202309024191300.csv'

# Check if file is found

def run_script():
    print("Execute Script")
    if os.path.isfile(path) == False:
        with open('data/Transaction_202309024191300.csv', 'w', newline = '') as file:
            writer_object = writer(file)
            writer_object.writerow(["transactionId", "productId", "transactionAmount", "transactionDatetime"])
            writer_object.writerow(make_a_transaction(1))
            file.close()

    else:
        # Logic to get the last integer for primary key
        last_row = pd.read_csv('data/Transaction_202309024191300.csv').tail(1)
        print(last_row)
        new_integer = last_row['transactionId'].values[0] + 1
        print(new_integer)
        
        with open('data/Transaction_202309024191300.csv', 'a', newline = '') as file:
            writer_object = writer(file)
            writer_object.writerow(make_a_transaction(new_integer))
            file.close()

def main():
    while True:
        run_script()
        time.sleep(300)

if __name__ == '__main__':
    main()