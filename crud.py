import pandas as pd
from json import loads, dumps

from datetime import datetime, timedelta

# Read and Join Data
def merge_tables():
    transactionData = pd.read_csv('C:/Users/tipan/OneDrive/Documents/Interviews/onebyzero/automation/transactions.csv')
    productData = pd.read_csv('data/ProductReference.csv')

    merged_tables = transactionData.merge(productData, on='productId', how='left')
    return merged_tables


# Transactions
def read_transaction_data(transaction_id : int):
    print(transaction_id)
    
    merged_data = merge_tables()
    
    merged_data['transactionId'] = merged_data['transactionId'].astype(int)
    merged_data['transactionId'] = merged_data['transactionId'].astype(str).str.strip() 

    filter_data = merged_data.loc[merged_data['transactionId'] == str(transaction_id)]
    print(filter_data)

    if not filter_data.empty:
        formatted_data = {
            "transactionId": int(filter_data['transactionId'].values[0]),
            "productName": filter_data['productName'].values[0],
            "transactionAmount": filter_data['transactionAmount'].values[0],
            "transactionDatetime": filter_data['transactionDatetime'].values[0]
        }
        return str(formatted_data)
    
    else:
        return "No matching transactions found for transaction_id: " + str(transaction_id)

# Summary by Products
def summary_by_products(last_n_days):
    merged_data = merge_tables()
    merged_data['transactionDatetime'] = pd.to_datetime(merged_data['transactionDatetime'])
    minus_x_days = datetime.now() - timedelta(int(last_n_days))
    filter_last_ten = merged_data[merged_data['transactionDatetime'] >= minus_x_days ]
    sum_prod_df = filter_last_ten[['transactionAmount', 'productName']].groupby(by="productName", dropna=False).sum()
    
    formatted_data = {
            "summary": [str(sum_prod_df.to_json(orient='columns'))]
    }
    return formatted_data

# Summary by City
def summary_by_city(last_n_days):
    merged_data = merge_tables()
    merged_data['transactionDatetime'] = pd.to_datetime(merged_data['transactionDatetime'])
    minus_x_days = datetime.now() - timedelta(int(last_n_days))
    filter_last_ten = merged_data[merged_data['transactionDatetime'] >= minus_x_days ]
    sum_city_df = filter_last_ten[['transactionAmount', 'productManufacturingCity']].groupby(by="productManufacturingCity", dropna=False).sum()
    
    formatted_data = {
            "summary": [str(sum_city_df.to_json(orient='columns'))]
    }
    return formatted_data