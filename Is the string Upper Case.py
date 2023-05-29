#Create a method to see whether the string is ALL CAPS.
#In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string
# ...containing no letters at all is trivially considered to be in ALL CAPS.

def is_uppercase(inp):
    special_characters={
        '%': "A",
        '$': "B",
        '&': "C"
    }

    spec_char_input = ""
    for char in inp:
        spec_char_input += special_characters.get(char, char)
    return spec_char_input.isupper()
