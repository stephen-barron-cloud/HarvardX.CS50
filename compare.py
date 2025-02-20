x = int(input("What should x be? "))
y = int(input("What should y be? "))

#Check work
# print(x, y)

# Option 2
print
if x < y:
    print("x is less than y")
elif x > y: 
    print("x is greater than y")
elif x == y:
    print ("X is equal to y")
print()

#Option 3
if x < y:
    print("x is less than y")
elif x > y: 
    print("x is greater than y")
else:
    print ("X is equal to y")
print()

#new question
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
print()

#new question 2
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
print()
