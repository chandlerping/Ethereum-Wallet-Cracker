from web3 import Web3


infura_url = 'https://mainnet.infura.io/v3/aca549ba6a054c5592860a067d90444b'
web3 = Web3(Web3.HTTPProvider(infura_url))


if web3.is_connected():
    print("Connected to Ethereum network")
else:
    print("Failed to connect to Ethereum network")


token_contract_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'
wallet_address = '0x8aAF720BBbcaC82c592Ac8f6c628bbaC1590e079'


token_abi = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    }
]


token_contract = web3.eth.contract(address=token_contract_address, abi=token_abi)


balance = token_contract.functions.balanceOf(wallet_address).call()


readable_balance = web3.from_wei(balance, 'ether')
print(f"Balance: {readable_balance} Tokens")
