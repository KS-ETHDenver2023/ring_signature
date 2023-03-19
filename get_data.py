import requests
import json
import pprint
import math
import binascii
import ecdsa

url = "	https://xrplcluster.com/"
p = 2**256 - 2**32 - 977

#get the latest tx from the ledger, return account address
def getLatestTx():
    payload = {
        "method": "tx_history",
        "params": [
            {
                "start": 5
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response)
    result = response.json()
    txs = result['result']['txs']
    accounts = []
    for i in range(len(txs)):
        accounts.append(txs[i]['Account'])
    return(accounts)

#get  the account Info, and if balance superior to treshold return the latest tx id to get the pub key
def getAccountInfo(treshold, account): 

    payload = {
        "method": "account_info",
        "params": [
            {
                "account": account
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    result = response.json()
    balance = result['result']['account_data']['Balance']
    if int(balance) > treshold :
        return result['result']['account_data']['PreviousTxnID']
    return("")

# return the pubkey (x points on secp256k1) from a tx hash
def getAccountKey(txId):

    payload = {
       "method": "tx",
    "params": [
        {
            "transaction": txId
        }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    result = response.json()
    pubKey = result['result']['SigningPubKey'][2:]
    print(pubKey)
    return pubKey
    
# get the couple x,y from an account
def get_y_from_x(hex_x):
    # Convert hex string to integer
    x = int(hex_x, 16)
    # Compute y-coordinate
    y = None
    try:
        y_squared = (x**3 +7) %p
        print(y_squared)
        y = ecdsa.numbertheory.square_root_mod_prime(y_squared, p)
    except:
        print("Error computing y-coordinate.")
    return(x,y)

#function to build the ring for the signature
def getRing():
    accountList = getLatestTx()
    tempoTxList=[]
    for i in range(len(accountList)): 
        tempo = getAccountInfo(5,accountList[i])
        if tempo !="" :
            tempoTxList.append(tempo)
    txList = list(set(tempoTxList))
    print(txList)
    points = []
    for i in range(len(txList)): 
        a = get_y_from_x(getAccountKey(txList[i]))
        points.append(a)
    return a

getRing()

