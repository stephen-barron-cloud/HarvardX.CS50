"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, 
as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, 
implement a program that prompts the user for a str of text and then outputs that same text but 
with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

def main():
    var_input = (input("Please enter a String:"))
    str_input = str(var_input)
    str_shortnmae = remove_vowels(str_input)
    print(str_shortnmae)

def remove_vowels(loc_input):
    s_output = str("")
    for char in loc_input:
        match char:
            case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
                continue
            case _:
                s_output = (s_output + char)
    return s_output


main()