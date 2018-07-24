# BlockchainSecurity

## otx_cli_tool
A tool that pulls relevant blockchain information from the OpenThreatExchange API. Built upon the Open Threat Exchange Python SDK at https://github.com/AlienVault-OTX/OTX-Python-SDK
 
  - Main script is 'otx_tool.py'
  - Requried dependencies: pandas, OTXv2.py
  
### OTX API GUIDE NOTES

- OTX reports on and receives threat data in the form of _pulses_.

- a _pulse_ consists of 1+ indicator of compromise (IOC) that constitute a threat or sequence of actions that could be used to carry out attacks on network devices/computers. 

- _pulses_ also provide information on the reliability of the threat info, who reported the threat, and other details of threat investigations

- OTX provides the 'DirectConnect SDK' for Python:
    https://github.com/AlienVault-OTX/OTX-Python-SDK

    - install with `pip install OTXv2`

- link to user guide for OTX: https://www.alienvault.com/documentation/resources/pdf/otx-user-guide.pdf
