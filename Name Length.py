name = input("What is your name? ")
name_length = len(name)

if name_length < 3:
    print("Name must be at least 3 characters")
elif name_length > 10:
    print("Name can be maximum of 10")
else:
    print("Name looks goods!")