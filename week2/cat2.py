#cat2.py

def main():
    x = get_number()
    meow(x)

def meow(w):
    for _ in range(w):
        print("Meow")

def get_number():
    while True:
        n = int(input("Input a number greater than 0: "))
        if n > 0:
            return n

main()