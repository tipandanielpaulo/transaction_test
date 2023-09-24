"""
This is used to produce dummy data
"""

import pandas as pd
from random import randrange
from datetime import datetime, timedelta

time_intervals = pd.date_range(start='2023-09-01 00:00:00', end='2023-09-23 23:55:00', freq='5T')

# Create a DataFrame with timestamps and corresponding values
data = {
    'transactionId': [i+1 for i in range(len(time_intervals))],
    'productId':  [randrange(10, 50, 10) for _ in range(len(time_intervals))],
    'transactionAmount': [randrange(1000, 5000, 1000) for _ in range(len(time_intervals))],
    'transactionDatetime':time_intervals
    
}

df = pd.DataFrame(data)

datenow = datetime.now().strftime("%Y%m%d%H%M%S")
df.to_csv(f'Transaction_{datenow}.csv', index=False)