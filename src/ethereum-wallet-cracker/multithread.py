import threading
import requests
import pandas as pd

###register many API keys
API_KEYs=[]

def fetch_transactions(public_key):
    api_key = "IWQXC4T1VHE7XMWI4KM9KQEZE9JET4P5ME" # multiple API key
    url = "http://api.etherscan.io/api"
   
    params = {
        "module": "account",
        "action": "txlist",
        "address": public_key,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": api_key
    }
    
 
    response = requests.get(url, params=params)
    
   
    if response.status_code == 200:
        
        transactions = response.json()
        return transactions
    else:
        return "Error: Unable to fetch transactions"

def csv_processor(Source):
    current_row=0
    while True:
        lock.acquire()
        if current_row >= len(Source):
            lock.release()
            break
        row_data = Source.iloc[current_row,0]
        print(row_data)
        #fetch_transactions(row_data)
        current_row += 1
        lock.release()


def many_thread(File):
    threads = []
    for _ in range(10):
        t = threading.Thread(target=csv_processor(File))
        threads.append(t)
        t.setDaemon(True) 
    for t in threads: 
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    lock=threading.Lock()
    dir='./keys.csv'
    Source = pd.read_csv(dir)
    many_thread((Source))
    print("thread end")