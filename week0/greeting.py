def greet(input):
    if "hello" in input:
        return "Hello there, " + "stove"
    else:
        return "I'm not sure what you mean"

input2 = input("Ello Mate! ")
greeting = greet(input2)
print(greeting)
