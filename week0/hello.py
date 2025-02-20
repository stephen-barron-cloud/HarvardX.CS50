# basic code assign variable, write prompt
#
#
#

"""
comment blocks
"""

var_name = input("what is your name? ")

#remove whitespace from str
var_name = var_name.strip()

# capitalize the first name
var_name = var_name.title()

# String together 
var_name = var_name.strip().title()

# same output
# concat into 1 argument

# 2 arguments
print("Hello,", var_name, sep=' | ', end='\n')

#changing variagles
print("Hello, ", end="")
print(var_name)

print('Hello, "friend"' )
print("Hello, \"friend\"")

# Fstrings
print(f"hello, {var_name}")

# Super short way of adding in the funcitions available on a string (str)
var_name = input("what is your name? ").strip().title()

# Split users name into firstname and lastname
var_first, var_last = var_name.split(" ")
print(f"hello, {var_first}")
# Print Parameters

#(function) def print(
#    *values: object,
#    sep: str | None = " ",
#    end: str | None = "\n",
#    file: SupportsWrite[str] | None = None,
#    flush: Literal[False] = False
#) -> None
#Prints the values to a stream, or to sys.stdout by default.
#
#sep
#  string inserted between values, default a space.
#end
#  string appended after the last value, default a newline.
#file
#  a file-like object (stream); defaults to the current sys.stdout.
#flush
#  whether to forcibly flush the stream.

