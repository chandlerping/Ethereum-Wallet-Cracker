import requests

def fetch_transactions(public_key):
    api_key = "IWQXC4T1VHE7XMWI4KM9KQEZE9JET4P5ME"
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


public_key = "0x81eE3A55A30F28195ee6e3df221506b9543Ec0Bb"
transactions = fetch_transactions(public_key)

if transactions['message']!= "No transactions found":
   
    for tx in transactions.get('result', []):
        print(tx)
        print(f"Block Number: {tx['blockNumber']}, Hash: {tx['hash']}")
else:
    print(transactions)
