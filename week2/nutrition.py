"""
n a file called nutrition.py, implement a program that prompts consumers users
to input a fruit (case-insensitively) and then outputs the number of calories in 
one portion of that fruit, per the FDA’s poster for fruits, which is also available as 
text. Capitalization aside, assume that users will input fruits exactly as written in the 
poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

Rather than use a conditional with 20 Boolean expressions, one for each fruit, better 
to use a dict to associate a fruit with its calories!
If k is a str and d is a dict, you can check whether k is a key in d with code like:

if k in d:
    ...


"""

def main():
    dict_nutrition = {
        "Apple" : 130,
        "Avocado" : 50,
        "Banana" : 110,
        "Cantaloupe" : 50,
        "Grapefruit" : 60,
        "Grapes" : 90,
        "Honeydew" : 50,
        "Kiwifruit" : 90,
        "Lemon" : 15,
        "Lime" : 20,
        "Nectarine" : 60,
        "Orange" : 80,
        "Peach" : 60,
        "Pear" : 100,
        "Pineapple" : 50,
        "Plums" : 70,
        "Strawberries" : 50,
        "Cherries" : 100,
        "Tangerine" : 50,
        "Watermelon" : 80
    }

    user_input = str(input("Please enter a fruit: ")).capitalize()

    print("Calories: ",dict_nutrition[user_input])

main()