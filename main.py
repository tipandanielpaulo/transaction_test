"""
FastAPI Application for Onebyzero
Date Created: 2023-09-22

Installation:
pip install "fastapi[all]", "uvicorn[standard]"

Use this code to run:
uvicorn main:app --host 0.0.0.0 --port 80  & python transactions.py
"""

from fastapi import FastAPI
import uvicorn, os

from datetime import datetime

from crud import read_transaction_data, summary_by_products, summary_by_city


app = FastAPI()

@app.get("/")
def root():
    """
    Home Page
    """
    return {"message": "Onebyzero"}

# GET Transactions
@app.get("/assignment/transaction/{transaction_id}")
def get_transactions_data(transaction_id):
    """
    Gives Transaction Data:
    Output data JSON: { 
        "transactionId": 1, 
        "productName": "P1", 
        "transactionAmount": 1000.0, 
        "transactionDatetime": "2018-01-01 10:10:10"
    }
    """
    return read_transaction_data(transaction_id)

# GET Transaction Summary By Products
@app.get("/assignment/transactionSummaryByProducts/{last_n_days}")
def get_transactions_summary_products(last_n_days):
    """
    Gives Transaction Data:
    Output data JSON: { "summary": [ 
        {"productName": "P1", 
        "totalAmount": 3000.0}
        ]
    }
    """
    return summary_by_products(last_n_days)

# GET Transaction Summary By Manufacturing City
@app.get("/assignment/transactionSummaryByManufacturingCity/{last_n_days}")
def get_transactions_summary_manufacturing(last_n_days):
    """
    Gives Transaction Data:
    Output data JSON: {"summary": [
        "cityName": "C1", 
        "totalAmount": 3000.0}
        ]
    }
    """
    return summary_by_city(last_n_days)


if __name__ == "__main__":
    uvicorn.run(app, port=int(os.environ.get("PORT", 8080)), host="0.0.0.0")