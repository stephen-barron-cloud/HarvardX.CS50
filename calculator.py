## calculator.py
## input from keyboard is a str by default

e = input("what is x? ")
f = input("what is y? ")

print(float(e) + float(f))
z = round(float(e) + float(f))
print(z)

## method 2 (shorter), defines the variable as an integer 
x = int(input("what is x? "))
y = int(input("what is y? "))

print(x + y)

## method 3, probably hardest to read, too complex but possible
print( int(input("what is x? ")) + int(input("what is y? ")))


e = input("what is x? ")
f = input("what is y? ")

print(float(e) + float(f))
z = round(float(e) + float(f))
print(f"{z:,}")


## rounding floats to specific decimal places
e = float(input("what is x? "))
f = float(input("what is y? "))
z = e / f

z = round(e / f, 2)
print(f"{z:.2f}")

print(z)