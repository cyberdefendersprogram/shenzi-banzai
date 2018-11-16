from otx_tool import pulse_print
from to_send import tools

otx = OTXv2(otxKey) # Initializes session with OTXv2 API using key contained in secrets.py


print ('-' * 40)
print (" S H E N Z I")
print ('-' * 40)
print ("1. Command Line Report")
print ("2. Email Report")
print ("3. Exit")
print ('-' * 40)

choice = int(input('[1-3]?:'))

if choice == 1:
    pulse_print()
elif choice == 2:
    tools()
elif choice == 3:
    SystemExit()
else:
    print("Invalid number. Try again...")