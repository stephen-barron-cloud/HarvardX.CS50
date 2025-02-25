"""
In a file called camel.py, implement a program that prompts the user for the name of a variable in camel 
case and outputs the corresponding name in snake case. Assume that the user’s 
input will indeed be in camel case.
"""

def main():
    var_input = (input("Please enter a variable name in Camel Case:"))
    str_input = str(var_input)
    str_snake_case = camel_to_snake(str_input)
    print(str_snake_case)

def camel_to_snake(cc_input):
    s_output = str("")
    i = int(1)
    for char in cc_input:
       #print(char)
        # Lowercase first letter if needed
        if i == 1:
            i += 1
            s_output = str(char).lower()
        #if other letters are capitalized, change from X to _x
        elif str(char).isupper() == True:
            s_output = str(s_output) + "_" + str(char).lower()
        # is lowercase already
        else:
            s_output = str(s_output) + char
            i +=1
    return s_output

main()