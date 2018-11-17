from secrets import otxKey
from OTXv2 import OTXv2
import argparse
import sys

# time = str(datetime.now() - timedelta()) # Time at which script was initiated.

args = argparse.ArgumentParser()

args.add_argument('-d', '--description',
                    const='description',
                    action='append_const',  
                    dest='optList',
                    default=[],
                    help='returns description of each pulse')
args.add_argument('-t', '--tags',
                    const='tags',
                    action='append_const',
                    dest='optList',
                    default=[],
                    help='returns tags for each pulse')
args.add_argument('-m', '--modified',
                    const='modified',
                    action='append_const',
                    dest='optList',
                    default=[],
                    help='return date modified for each pulse')
args.add_argument('-i', '--id',
                    const='id',
                    action='append_const',
                    dest='optList',
                    default=[],
                    help='return pulse ids')
args.add_argument('-au', '--author_name',
                    const='author_name',
                    action='append_const',
                    dest='optList',
                    default=[],
                    help='return author\'s name for each pulse') 
args.add_argument('-ad', '--adversary',
                    const='adversary',
                    action='append_const',
                    dest='optList',
                    default=[],
                    help='return adversary title for pulses')
args.add_argument('-ref', '--references',
                    const='references',
                    action='append_const',
                    dest='optList',
                    default=[],
                    help='return each pulses references')
args.add_argument('-rev', '--revisions',
                    const='revisions',
                    action='append_const',
                    dest='optList',
                    default=[],
                    help='return pulse revisions')
args.add_argument('search',
                    metavar='SEARCH QUERY',
                    type=str,
                    help='list search term',
                    default='crypto')

options = args.parse_args()

print(options.optList)

try:
    otx = OTXv2(otxKey) # Initializes session with OTXv2 API using key contained in secrets.py
except: 
    print("problem with API key")

pulses = otx.search_pulses(options.optList, 40) # Retrieves list (in json format) of top 40 pulses with tag "crypto"

def pulse_print(): # Loops through each individual pulse retrieved from OTX, and prints name & requested fields.
    for aPulse in pulses["results"]:
        print('[+] '+'Pulse Name: '+aPulse.get('name')+'\n')
        for switch in options:
            try:
                print('[+] '+switch.title()+': '+aPulse.get(switch)+'\n')
            except:
                print()
        print('-'*30)
    print()