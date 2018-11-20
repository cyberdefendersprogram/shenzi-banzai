# This is the main script for the Banzai blockchain security assessment.

from urllib.request import urlopen, Request
import json

class crypto51():

''' coin_attr is the main method for crypto51. To call, give coin name as argument and then '1's as on flags for algorithm, hash rate, hourly attack cost, and nicehashable percentage.
'''

    def __init__(self):

        C51_URL = 'https://www.crypto51.app/coins.json'
        C51_REQ = Request(C51_URL, headers={'User-Agent': 'Mozilla/5.0'})
        URL_BYTE = urlopen(C51_REQ).read() # Pull Crypto51 url
        URL_STR = URL_BYTE.decode('utf-8') # Decode byte object from URL into URL string
        C51_JSON = json.loads(URL_STR) # Loads URL string as a JSON object
        self.COINS_DATA = C51_JSON['coins'] # Clean JSON so that it starts at most convenient level, 'coins'

    def coins_data(self):
        # Returns full JSON object for coin info
        return self.COINS_DATA

    def coin_attr(self, coin_name, algorithm=0, hash_rate=0, hourly_attack_cost=0, nicehashable=0):
        # Based on arguments given, loops through full coin info JSON and picks out requested coin,
        # and requested information for that coin.
        attr = {}
        attr['name'] = coin_name
        for coinDict in self.COINS_DATA:
            if coinDict['name'] == attr['name']:
                if algorithm==1:
                    attr['algorithm'] = coinDict['algorithm']
                if hash_rate==1:
                    attr['hash_rate'] = coinDict.get('hash_rate')
                if hourly_attack_cost==1:
                    attr['hourly_attack_cost'] = coinDict.get('attack_hourly_cost_pretty')
                if nicehashable==1:
                    nicehashable = coinDict.get('network_vs_rentable_ratio')
                    nicehashable = nicehashable*100
                    attr['nicehashable'] = str(round(nicehashable,2)) + '%'
        return attr
