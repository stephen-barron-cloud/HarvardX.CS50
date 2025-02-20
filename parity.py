
#Option 2
def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
# Option 1    
#    if n % 2 == 0:
#        return True
#    else:
#        return False

# Option 2
#    return True if n % 2 == 0 else False

# Option 3
    return n % 2 == 0

main()

