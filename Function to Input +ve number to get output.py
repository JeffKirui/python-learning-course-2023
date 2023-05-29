def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        i = int(input("How many times? "))
        if i > 0:
            break
    return i


def meow(i):
    for _ in range(i):
        print("Meow")


main()
