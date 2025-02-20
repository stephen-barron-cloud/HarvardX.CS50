name = input("what's your name? ")

# Option 1
if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else: 
    print("Hufflepuff")

# Option 2
if name == "Harry" or name =="Hermoine" or name ==  "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else: 
    print("Hufflepuff")

#Option 3
# Match
match name:
    case "Harry" | "Hermoine" | "Ron" | "Neville":
        print("Gryffindor")
    case "Draco":
        print("Slythern")
    case _:
        print("Hufflepuff")