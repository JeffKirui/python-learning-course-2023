command = ""
started = False

while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started. What are you doing?")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("The car is already stopped. What are you doing?")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit""")
    elif command == "quit":
        break
    else:
        print("I dont understand that!")