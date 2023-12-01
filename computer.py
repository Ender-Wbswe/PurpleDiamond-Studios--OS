def clear():
    time = 100
    while time != 0:
        print(".")
        time-=1
    return
controlsTop = "Controls: Type \"down\" to move cursor down, \"ok\" to select:"
controlsMid = "Controls: Type \"down\" to move cursor down, \"up\" to move cursor up, \"ok\" to select:"
controlsEnd = "Controls: Type \"up\" to move cursor up, \"ok\" to select"
def calculator():
    clear()
    print("Calculator open")
    print("Type \"exit\" when asked for \"Operation\" to leave")
    num1 = float(input("Number: "))
    operation = input("Operation(+,-,*,/,^): ")
    num2 = float(input("Number: "))
    while True:
        if "exit" in operation.lower():
            break
        elif "+" in operation:
            num3 = num1 + num2
            print("=",num3)
        elif "-" in operation:
            num3 = num3 = num1 - num2
            print("=",num3)
        elif "*" in operation:
            num3 = num1 * num2
            print("=",num3)
        elif "/" in operation:
            num3 = num1 / num2
            print("=",num3)
        elif "^" in operation:
            time = int(num2)
            num3 = num1
            while time != 0:
                num3 *= num1
                time -=1
            print("=",num3)
        else:
            print("Invalid operation, returning home")
            clear()
        num1 = float(num3)
        operation = input("Operation(+,-,*,/,^): ")
        if "exit" in operation:
            break
        else:
            pass
        num2 = float(input("Number: "))
    clear()
    return
def usersGuide():
    print("Hello, welcome to the User's Guide!")
    print("Type \"back\" to exit")
    print("Current entries are: Calculator(or 'calc' if you are in a hurry), Games, Tools")
    learn = input("What do you want to learn about?: ")
    while True:
        if "back" in learn.lower():
            break
        elif "calc" in learn.lower():
            clear()
            print("Calculator:\nThe Calculator is able to do five operations, adding, subtracting, multiplying, dividing, and exponentials.")
            print("The way it works:\nIt will first ask for a number, then what operation you need,then the next number.\nIt will cycle between the two until you type\"exit\".\n")
            input(">>")
            clear()
        elif "game" in learn.lower():
            clear()
            print("Game One: Letter Guessing Game, where you have three tries to guess a rendom letter, chosen by the program.\nGame Two: A text-based adventure\n")
            input(">>")
            clear()
        elif "tool" in learn.lower():
            clear()
            print("Tool One: Text to Text Art tool, it does what you think it does\n")
            input(">>")
            clear()
        else:
            print("No entry for \"" + learn + "\" found")
            input(">>")
            clear()
        
        print("Type \"back\" to exit")
        print("Current entries are: Calculator(or 'calc' if you are in a hurry), Games, Tools")
        learn = input("What do you want to learn about?: ")
    clear()
    return
def games():
    selected1 = "Games:\n\nLetter Guessing Game<\n\nText-Based Adventure\n\nBack\n" + controlsTop
    selected2 = "Games:\n\nLetter Guessing Game\n\nText-Based Adventure<\n\nBack\n" + controlsMid
    selected3 = "Games:\n\nLetter Guessing Game\n\nText-Based Adventure\n\nBack<\n" + controlsEnd
    now = selected1
    while True:
        while now == selected1:
            print(selected1)
            command = input(">>")
            if "ok" in command:
                clear()
                games_letterGuessingGame()
            elif "down" in command:
                clear()
                now = selected2
            else:
                clear()
        while now == selected2:
            print(selected2)
            command = input(">>")
            if "down" in command:
                clear()
                now = selected3
            elif "up" in command:
                clear()
                now = selected1
            elif "ok" in command:
                clear()
                games_textAdventure_Menu()
            else:
                clear()
        while now == selected3:
            print(selected3)
            command = input(">>")
            if "ok" in command:
                clear()
                now = "no"
                break
            elif "up" in command:
                clear()
                now = selected2
            else:
                clear()
        if now == "no":
            break
    return
def games_letterGuessingGame():
    while True:
        print("Guess the Letter!")
        abc = "qwertyuiopasdfghjklzxcvbnm"
        import random
        answer = random.choice(abc)
        guess = input("Enter your guess, you get three chances: ")
        time = 2
        while time != 0:
            if guess.lower() in answer.lower():
                print("You win!")
                break
            else:
                guess = input("Try again: ")
                time -=1
        retry = input("Try again?(yes/no): ")
        if "no" in retry.lower():
            break
        else:
            pass
    clear()
    return
def games_textAdventure_Menu():
    selected1 = "Welcome to [textAdventure]!\nby PurpleDiamond Studios\n\nPlay<\n\nExit Game\n" +controlsTop
    selected2 = "Welcome to [textAdventure]!\nby PurpleDiamond Studios\n\nPlay\n\nExit Game<\n" +controlsEnd
    now = selected1
    while True:
        while now == selected1:
            print(selected1)
            command = input(">>")
            if "down" in command:
                clear()
                now = selected2
            elif "ok" in command:
                clear()
                games_textAdventure_game()
            else:
                clear()
        while now == selected2:
            print(selected2)
            command = input(">>")
            if "up" in command:
                clear()
                now = selected1
            if "ok" in command:
                now = "no"
                break
        if now == "no":
            clear()
            return
def games_textAdventure_game():
    print("Game not finished yet")
    input(">>")
    clear()
    return
def tools():
    selected1 = "\nTools:\n\nNumber to Text Art<\n\nBack\n\n" + controlsTop
    selected2 = "\nTools:\n\nNumber to Text Art\n\nBack<\n\n" + controlsEnd
    now = selected1
    while True:
        while now == selected1:
            print(selected1)
            command = input(">>")
            if "down" in command.lower():
                clear()
                now = selected2
            elif "ok" in command.lower():
                clear()
                tools_numberToTextArt()
            else:
                clear()
        while now == selected2:
            print(selected2)
            command = input(">>")
            if "up" in command.lower():
                clear()
                now = selected1
            elif "ok" in command.lower():
                now = "no"
                break
            else:
                clear()
        if now == "no":
            break
    return
def tools_numberToTextArt():
    def numbersShadow():
        while True:
            number =  input("\"back\" to go back\nWhat number do you want converted? Single digits only.\n>>")
            if "back" in number.lower():
                break
            elif number == "1":
                print() #gaps to give space
                print(" ██╗")
                print("███║")
                print("╚██║")
                print(" ██║")
                print(" ██║")
                print(" ╚═╝")
                print()
            elif number == "2":
                print()
                print("██████╗ ")
                print("╚════██╗")
                print(" █████╔╝")
                print("██╔═══╝ ")
                print("███████╗")
                print("╚══════╝")
                print()
            elif number == "3":
                print()
                print("██████╗ ")
                print("╚════██╗")
                print(" █████╔╝")
                print(" ╚═══██╗")
                print("██████╔╝")
                print("╚═════╝ ")
                print()
            elif number == "4":
                print()
                print("██╗  ██╗")
                print("██║  ██║")
                print("███████║")
                print("╚════██║")
                print("     ██║")
                print("     ╚═╝")
                print()
            elif number == "5":
                print()
                print("███████╗")
                print("██╔════╝")
                print("███████╗")
                print("╚════██║")
                print("███████║")
                print("╚══════╝")
                print()
            elif number == "6":
                print()
                print(" ██████╗ ")
                print("██╔════╝ ")
                print("███████╗ ")
                print("██╔═══██╗")
                print("╚██████╔╝")
                print(" ╚═════╝ ")
                print()
            elif number == "7":
                print()
                print("███████╗")
                print("╚════██║")
                print("    ██╔╝")
                print("   ██╔╝ ")
                print("   ██║ ")
                print("   ╚═╝  ")
                print()
            elif number == "8":
                print()
                print(" █████╗ ")
                print("██╔══██╗")
                print("╚█████╔╝")
                print("██╔══██╗")
                print("╚█████╔╝")
                print(" ╚════╝ ")
                print()
            elif number == "9":
                print()
                print(" █████╗ ")
                print("██╔══██╗")
                print("╚██████║")
                print(" ╚═══██║")
                print(" █████╔╝")
                print(" ╚════╝ ")
                print()
            elif number == "0":
                print()
                print(" ██████╗ ")
                print("██╔═████╗")
                print("██║██╔██║")
                print("████╔╝██║")
                print("╚██████╔╝")
                print(" ╚═════╝ ")
                print()
            else:
                clear()
    def numbers3d():
        while True:
            number =  input("\"back\" to go back\nWhat number do you want converted? Single digits only. ")
            if "back" in number.lower():
                break
            elif number == "0":
                print()
                print(" ________      ")
                print("|\   __  \     ")
                print("\ \  \|\  \    ")
                print(" \ \  \\\  \   ")
                print("  \ \  \\\  \  ")
                print("   \ \_______\ ")
                print("    \|_______| ")
                print()
            elif number == "1":
                print()
                print("  _____     ")
                print(" / __  \    ")
                print("|\/_|\  \   ")
                print("\|/ \ \  \  ")
                print("     \ \  \ ")
                print("      \ \__\ ")
                print("       \|__|")
                print()
            elif number == "2":
                print()
                print("  _______     ")
                print(" /  ___  \    ")
                print("/__/|_/  /|   ")
                print("|__|//  / /   ")
                print("    /  /_/__  ")
                print("   |\________\ ")
                print("    \|_______|")
                print()
            elif number == "3":
                print()
                print(" ________     ")
                print("|\_____  \    ")
                print("\|____|\ /_   ")
                print("      \|\  \  ")
                print("     __\_\  \ ")
                print("    |\_______\ ")
                print("    \|_______|")
                print()
            elif number == "4":
                print()
                print(" ___   ___     ")
                print("|\  \ |\  \    ")
                print("\ \  \\_\  \   ")
                print(" \ \______  \  ")
                print("  \|_____|\  \ ")
                print("         \ \__\ ")
                print("          \|__|")
                print()
            elif number == "5":
                print()
                print(" ________      ")
                print("|\   ____\     ")
                print("\ \  \___|_    ")
                print(" \ \_____  \   ")
                print("  \|____|\  \  ")
                print("    ____\_\  \ ")
                print("   |\_________\ ")
                print("   \|_________|")
                print
            elif number == "6":
                print()
                print(" ________     ")
                print("|\   ____\    ")
                print("\ \  \___|    ")
                print(" \ \  \____   ")
                print("  \ \  ___  \ ")
                print("   \ \_______\ ")
                print("    \|_______|")
                print()
            elif number == "7":
                print()
                print(" ________  ")
                print("|\_____  \ ")
                print(" \|___/  /|")
                print("     /  / /")
                print("    /  / / ")
                print("   /__/ /  ")
                print("   |__|/   ")
                print()
            elif number == "8":
                print()
                print(" ________     ")
                print("|\   __  \    ")
                print("\ \  \|\  \   ")
                print(" \ \   __  \  ")
                print("  \ \  \|\  \ ")
                print("   \ \_______\ ")
                print("    \|_______|")
                print()
            elif number == "9":
                print()
                print(" ________     ")
                print("|\  ___  \    ")
                print("\ \____   \   ")
                print(" \|____|\  \  ")
                print("     __\_\  \ ")
                print("    |\_______\ ")
                print("    \|_______|")
                print()
            else:
                clear()
    print("Input to Text Art")
    print("Supported characters: 1,2,3,4,5,6,7,8,9,0")
    font =  input("What font do you want? Your options are Shadow, 3d\n>>")
    if "shadow" in font.lower():
        clear()
        numbersShadow()
    elif "3d" in font.lower():
        clear()
        numbers3d()
clear()
print("\nWelcome!")
select1 = "\nApps:\n\n\tCalculator<\n\n\tUser's Guide\n\n\tGames\n\n\tTools\n\nLeave\n\n" + controlsTop
select2 = "\nApps:\n\n\tCalculator\n\n\tUser's Guide<\n\n\tGames\n\n\tTools\n\nLeave\n\n" + controlsMid
select3 = "\nApps:\n\n\tCalculator\n\n\tUser's Guide\n\n\tGames<\n\n\tTools\n\nLeave\n\n" + controlsMid
select4 = "\nApps:\n\n\tCalculator\n\n\tUser's Guide\n\n\tGames\n\n\tTools<\n\nLeave\n\n" + controlsMid
select5 = "\nApps:\n\n\tCalculator\n\n\tUser's Guide\n\n\tGames\n\n\tTools\n\nLeave<\n\n" + controlsEnd
current = select1
while True:
    while current == select1:
        print(select1,end="",flush=True)
        command = input(">>")
        if "down" in command.lower():
            clear()
            current = select2
        elif "ok" in command.lower():
            calculator()
        else:
            clear()
            clear()
    while current == select2:
        print(select2)
        command = input(">>")
        if "down" in command.lower():
            clear()
            current = select3
        elif "up" in command.lower():
            clear()
            current = select1
        elif "ok" in command.lower():
            clear()
            usersGuide()
        else:
            clear()
            clear()
    while current == select3:
        print(select3)
        command = input(">>")
        if "down" in command.lower():
            clear()
            current = select4
        elif "up" in command.lower():
            clear()
            current = select2
        elif "ok" in command.lower():
            clear()
            games()
        else:
            clear()
            clear()
    while current == select4:
        print(select4)
        command = input(">>")
        if "down" in command.lower():
            clear()
            current = select5
        elif "up" in command.lower():
            clear()
            current = select3
        elif "ok" in command.lower():
            clear()
            tools()
        else:
            clear()
            clear()
    while current == select5:
        print(select5)
        command = input(">>")
        if "up" in command.lower():
            clear()
            current = select4
        elif "ok" in command.lower():
            current = "no"
        else:
            clear()
            clear()
    if current == "no":
        break
clear()
print("Goodbye!")            