"""
In a file called bank.py, 
implement a program that prompts the user for a greeting. 
If the greeting starts with “hello”, output $0. 
If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. 
Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

"""
def main():
    greeting = (input("Please type a greeting. ")).lstrip().lower()
    greetingstart = greeting.startswith("h")
    
    if greeting == "hello":
        print("$0")
    elif greetingstart == True:
        print ("$20")
    else:
        print("$100")


main()