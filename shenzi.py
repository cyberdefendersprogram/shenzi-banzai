from shenzi_helpers import crypto51
import coinSecureRating

staleRates = {'Bitcoin':(0.41), 'Ethereum':(6.8), 'Litecoin':(0.273), 'Dogecoin':(0.619)}

blockchains =   ['Bitcoin',
                'Ethereum',
                'Bitcoin Cash',
                'Litecoin',
                'Monero',
                'Ethereum Classic',
                'Dash',
                'Zcash',
                'Bytecoin',
                'Dogecoin',
                'Metaverse ETP',
                'Monacoin',
                'ZenCash',
                'Bitcoin Private',
                'ZClassic',
                'Electroneum',
                'Vertcoin',
                'Unobtanium',
                'Ubiq',
                'Blockchain Interest',
                'Litecoin Cash',
                'Viacoin',
                'Einsteinium',
                'Gulden',
                'Quantum Resistant Ledger',
                'PACcoin',
                'GameCredits',
                'LBRY Credits',
                'Feathercoin',
                'Bulwark',
                'Pascal Coin',
                'Crown',
                'BitConnect',
                'Expanse',
                'DNotes',
                'SIBCoin',
                'FlorinCoin',
                'Mooncoin',
                'MonetaryUnit',
                'Myriad',
                'Musicoin',
                'BitcoinZ',
                'Graft',
                'GoByte',
                'Pirl',
                'Catcoin',
                'PinkCoin',
                'Auroracoin',
                'Universal Currency',
                'GeoCoin',
                'Sumokoin',
                'CannabisCoin',
                'Karbo',
                'Galactrum',
                'Hush',
                'TrezarCoin',
                'VIVO',
                'Monoeci',
                'MAZA',
                'STRAKS',
                'Ellaism',
                'Onix',
                'Innova',
                'Zetacoin',
                'Bata',
                'Cream',
                'Quark',
                'Rupee',
                'CryCash',
                'CrowdCoin',
                'Orbitcoin',
                'Adzcoin',
                'Deutsche eMark',
                'Startcoin',
                'WorldCoin',
                'Halcyon',
                'Linx',
                'SmartCoin',
                'Influxcoin',
                'Pascal Lite',
                'Prime-XI',
                'SOILcoin',
                'Phoenixcoin',
                'Pixie Coin',
                'Monero Original',
                'Commercium'
                ] # list of supported blockchains

print()
coinName = input("Please enter cryptocurrency (type 'list' to show supported coins): ")

def coinCheckandPrint(coinName):
    
    if coinName in blockchains:
        coinAttributes = crypto51().coin_attr(coinName, 1, 0, 1, 1)
        formattedCoinName = coinAttributes.get('name')
        print()
        print("[*] Name: {}".format(coinAttributes.get('name')))
        print()
        print("[*] Hash algorithm: {}".format(coinAttributes.get('algorithm')))
        print()
        print("[*] Price of 51% attack: {} ".format(coinAttributes.get('hourly_attack_cost')))
        print()
        print("[*] Percentage of necessary hash power available on NiceHash.com: {} ".format(coinAttributes.get('nicehashable')))
        print()
        if coinAttributes.get('name') in staleRates.keys():
            print("[*] Stale rate: {}".format(staleRates.get(formattedCoinName))+"%")
            print()

    elif coinName == 'list':
        print()
        print('-----List of available blockchains-----')
        print()
        for i in blockchains:
            print(i+'\n')

    else:
        print()
        print('Coin not found, please check spelling.')
        print()

try:
    coinCheckandPrint(coinName)
except:
    print('Exiting...')
