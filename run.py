import subprocess
import time

# Transactions
transactions_script = "python transactions.py"

# FastAPI application
uvicorn_command = "uvicorn main:app --host 0.0.0.0 --port 80"


transactions_process = subprocess.Popen(transactions_script, shell=True)

time.sleep(5)


uvicorn_process = subprocess.Popen(uvicorn_command, shell=True)

uvicorn_process.wait()
transactions_process.wait()