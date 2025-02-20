"""
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression 
and then calculates and outputs the result as a floating-point value formatted to one decimal place.
 Assume that the user’s input will be formatted as x y z, with one space between x and y and one space 
 between y and z, wherein:

    x is an integer
    y is +, -, *, or /
    z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /,
 then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an 
interpreter for math!
"""

def main():
    var_userEquation = str (input("please enter an arithmetic expression in the format X <function> y where function is +,-,*,/. Example 1 + 3:  "))

    x,y,z = var_userEquation.split(sep=" ")
    xf = float(x)
    xz = float
    match y:
        case "+":
            var_n = round(float(x) + float(z),1)  
        case "-":
            var_n = round(float(x) - float(z),1)  
        case "/":
            var_n = round(float(x) / float(z),1)  
        case "*":
            var_n = round(float(x) * float(z),1)  
        case _:
            print("ERROR UNDEFINED")

    print("The answer to your equation is: ",var_n,".",sep="")
main()