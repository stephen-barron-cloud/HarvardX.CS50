
def main():
    height = 3
    width = 40
    size = 3
    # print_block(height)
    # print_row(width)
    print_rectangle(height,width)

def print_block(input):
    for _ in range(input):
        print("#")

def print_row(width):
    print("#" * width)


## Nested loops 
def print_rectangle(height,width):
# for each row in rectangle
    for i in range(height):
        # for each brick in row
        for j in range(width):
            # print brick
            print("#", end="")
        # next row
        print()



main()