
import sys

def reverse_string(string):
    str_list = string.partition(" ")
    updated_string = ''

    for data in reversed(str_list):
        updated_string += str(data[::-1])

    return updated_string

if __name__ == '__main__':
    args = sys.argv
    if len(args) <=1:
        print("No input provided")
        exit()
    else:
        print(reverse_string(args[1]))
