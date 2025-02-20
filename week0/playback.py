"""
In a file called playback.py, implement a program in Python that prompts 
the user for input and then outputs that same input, 
replacing each space with ... (i.e., three periods).
""" 

def main():
    v_string = str(input(" User, please input some input:")).replace(" ", "...")
    print(v_string)
main()