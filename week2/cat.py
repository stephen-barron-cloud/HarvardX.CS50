# Loops do things repetitively
#
# print("meow") 
# print("meow") 
# print("meow")

# Loops 1, decrementing
def main():
    m = int(input("how many meows? "))
    while m > 0:
        print("meow ", end=", ")
        m = m - 1
    print()

main()

#Loops 2, incrementing

def main2():
    i = 0
    m = int(input("how many moos? "))
    while i < m:
        print("moo", end=", ")
        i += 1 # shortened
    print()

main2()

# Loops 3 (for)
def main3():
    m = int(input("how many woof? "))
    for _ in range(m - 1):
        print("woof, ", end = "")
    print("woof")

main3()

# print x times; consice but harder to read
def main4():
    m = int(input("how many oink? "))
    # print("oink, " * m, end="")
    print("oink\n" * m, end="")

main4()

# while True:

def main5():
    while True:
        n = int(input("What is n? - Checking to make sure greater than 0"))
        if n < 0:
            continue
        else:
            break

main5()


# shorter:  
def main6():
    while True:
        n = int(input("How many Neighs?"))
        if n > 0:
            break
    for _ in range(n):
        print("Neigh")

main6()