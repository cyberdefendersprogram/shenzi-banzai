from OTXv2 import OTXv2, InvalidAPIKey
from banzai_helpers import otx_pulse_print, otx_options_handler
from secrets import otxKey

try:
    otx = OTXv2(otxKey) # Initializes session with OTXv2 API using key contained in secrets.py
except InvalidAPIKey: 
    print("Invalid API key")

options = otx_options_handler()    

pulses_json = otx.search_pulses(options.optList, 40) # Retrieves JSON of 40 pulses from OTX.

selected_pulses = otx_pulse_print(options, pulses_json)