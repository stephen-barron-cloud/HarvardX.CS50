"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be 
    an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid 
if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s 
input will be uppercase. Structure your program per the below, wherein is_valid returns True if s 
meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to 
implement additional functions for is_valid to call (e.g., one function per requirement).
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str_plate):

    var_first_num = -1 # -1 means no number found; otherwise the first number in the string
    list_plate_char =[]
    int_plate_length = int(len(str_plate))
    j = 0
    for char in str_plate:
        list_plate_char.insert(j,char)
        j +=1
    
    i = 0
    while (var_first_num < 0) and (i < int_plate_length) :
        str_temp = list_plate_char[i]
        if str(str_temp).isnumeric() == True:
            var_first_num = i
        i +=1
    
    #Check the length
    bool_length = check_length(int_plate_length)
    if bool_length == False:
        return False
    
    # see if the first two charaters are not numeric
    bool_first_two_chars = check_first_two_chars(var_first_num)
    if bool_first_two_chars == False:
        return False
    
    # See if first number is 0
    if var_first_num > 0:
        bool_first_num_0 = check_first_num_0(int(list_plate_char[var_first_num]))
        if bool_first_num_0 == False:
            return False

    # Check to make sure each character after the first number are also numbers
    bool_letters_after_numbers = check_letters_after_numbers(list_plate_char,var_first_num,int_plate_length)
    if bool_letters_after_numbers == False:
        return False
    
    # if all flags are true, return true
    return True
    
def check_length(plate):
    # print(int_length)
    if 2 <= plate <=6:
        return True
    else: return False

def check_first_two_chars(i):
    if (i == 0) or (i == 1):
        return False
    else: return True

def check_first_num_0(int_i):
    if int_i == 0:
        return False
    else: return True

def check_letters_after_numbers(list_l,int_i,plate_len):
    last_index = plate_len -1

    if int_i == -1: return True
    while int_i <= last_index:
        str_temp = str(list_l[int_i])
        if str_temp.isnumeric() != True:
            return False
        int_i +=1
    return True



main()