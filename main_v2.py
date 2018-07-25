from otx_tool import pulse_print
from sendemail import sendemail

def main():
    print ('-' * 40)
    print ("   M A I N - M E N U")
    print ('-' * 40)
    print ("1. Default and Command Line Options")
    print ("2. Search topic and send Email")
    print ("3. Exit")
    print ('-' * 40)
   
    choice = input('Enter your choice [1-3] : ')
    
    choice = int(choice)
    
    if choice == 1:
        pulse_print()
    elif choice == 2:
        tools()
    elif choice == 3:
        SystemExit()
    else:
        print("Invalid number. Try again...")
main()
