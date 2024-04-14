import socket
import requests
import socks

socks.set_default_proxy(socks.SOCKS5,"localhost",9050)
socket.socket=socks.socksocket


api_key = "IWQXC4T1VHE7XMWI4KM9KQEZE9JET4P5ME"
url = "http://api.etherscan.io/api"

params = {
    "module": "account",
    "action": "txlist",
    "address": "0xD061969E300085dCA5088c2b143c73d6617bc7E4",
    "startblock": 0,
    "endblock": 99999999,
    "sort": "asc",
    "apikey": api_key
}
response = requests.get(url,params=params)
print(response.json())
