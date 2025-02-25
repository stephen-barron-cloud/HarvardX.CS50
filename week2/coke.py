"""
In a file called coke.py, implement a program that prompts the user to insert a coin, 
one at a time, each time informing the user of the amount due. Once the user has 
inputted at least 50 cents, output how many cents in change the user is owed. Assume 
that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

def main():
    total_input = int(0)
    print("Cokes are 50 Cents")
    while total_input < 50:
        total_input += int(get_coin())
    int_change = total_input - 50
    print("Coke Dispensed")
    print("Change in cents Returned: ", int_change)


def get_coin():
    user_coin = 0
    while (user_coin != 5 and user_coin != 10 and user_coin != 25):
        user_coin = int(input("Please insert a coin, 5, 10, or 25 cents:  "))
    return user_coin

main()