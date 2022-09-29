import time, random
working = "yes"
print("Hello!")
time.sleep(2)
print("Welcome to math riddler!")
while working == "yes":
    time.sleep(2)
    print("Choose what you want a riddle of:")
    print("Options: \"adding\", \"multiplying\", \"subtracting\", \"exit\".")
    option = input("(type in an option just like its written above without quotes): ")
    if option == "adding":
        print("What numbers do you want to have in your riddles?")
        print("(options: unities, tens, hundreds, thousands, tens of thousands, hundreds of thousands")
        numbers = input("(type in an option): ")
        if numbers == "unities":
            numbers = 9
        elif numbers == "tens":
            numbers = 99
        elif numbers == "hundreds":
            numbers = 999
        elif numbers == "thousands":
            numbers = 9999
        elif numbers == "tenthousands":
            numbers = 99999
        elif numbers == "hundredthousands":
            numbers = 999999
        time.sleep(2)
    
        wrong = 0
        correct = 0
        WorkState = "ok"

        while WorkState != "exit":
        
            numbers = int(numbers)
            add = random.randint(1, numbers)
            addto = random.randint(1, numbers)
            checkStr = False
            while checkStr == False:
                print(add, "+", addto, "= ?" )
                result = input("(type in the result (number), \"exit\" without the quotes to end riddles): ")
                if any(str.isdigit(c) for c in result) == False:
                    if result == "exit":
                        WorkState = "exit"
                        checkStr = True
                        print("Correct answers: ", correct, ", Wrong answers:", wrong, ".")
                    else:
                        print("You typed in a text, not a number.")
                elif any(str.isdigit(c) for c in result) == True:
                    result = int(result)
                    if result == (add + addto):
                        print("Correct!")
                        correct += 1
                        checkStr = True
                    elif result != (add + addto):
                        print("Wrong.")
                        wrong += 1
                        checkStr = True
    elif option == "exit":
        print("Exiting...")
        working = "no"
    elif option == "multiplying":
        print("What numbers do you want to have in your riddles?")
        print("(options: unities, tens, hundreds, thousands, tens of thousands, hundreds of thousands")
        numbers = input("(type in an option): ")
        if numbers == "unities":
            numbers = 9
        elif numbers == "tens":
            numbers = 99
        elif numbers == "hundreds":
            numbers = 999
        elif numbers == "thousands":
            numbers = 9999
        elif numbers == "tenthousands":
            numbers = 99999
        elif numbers == "hundredthousands":
            numbers = 999999
        time.sleep(2)
    
        wrong = 0
        correct = 0
        WorkState = "ok"

        while WorkState != "exit":
        
            numbers = int(numbers)
            multiply = random.randint(1, numbers)
            multiplyBy = random.randint(1, numbers)
            checkStr = False
            while checkStr == False:
                print(multiply, "*", multiplyBy, "= ?" )
                result = input("(type in the result (number), \"exit\" without the quotes to end riddles): ")
                if any(str.isdigit(c) for c in result) == False:
                    if result == "exit":
                        WorkState = "exit"
                        checkStr = True
                        print("Correct answers: ", correct, ", Wrong answers:", wrong, ".")
                    else:
                        print("You typed in a text, not a number.")
                elif any(str.isdigit(c) for c in result) == True:
                    result = int(result)
                    if result == (multiply * multiplyBy):
                        print("Correct!")
                        correct += 1
                        checkStr = True
                    elif result != (multiply * multiplyBy):
                        print("Wrong.")
                        wrong += 1
                        checkStr = True
    elif option == "subtracting":
        print("What numbers do you want to have in your riddles?")
        print("(options: unities, tens, hundreds, thousands, tenthousands, hundredthousands")
        numbers = input("(type in an option): ")
        if numbers == "unities":
            numbers = 9
        elif numbers == "tens":
            numbers = 99
        elif numbers == "hundreds":
            numbers = 999
        elif numbers == "thousands":
            numbers = 9999
        elif numbers == "tenthousands":
            numbers = 99999
        elif numbers == "hundredthousands":
            numbers = 999999
        time.sleep(2)
    
        wrong = 0
        correct = 0
        WorkState = "ok"

        while WorkState != "exit":
        
            numbers = int(numbers)
            subtract = random.randint(1, numbers)
            subtractFrom = random.randint(1, numbers)
            checkStr = False
            while checkStr == False:
                print(substract, "-", substractFrom, "= ?" )
                result = input("(type in the result (number), \"exit\" without the quotes to end riddles): ")
                if any(str.isdigit(c) for c in result) == True: 
                    result = int(result)
                    if result == (subtract - subtractFrom):
                        print("Correct!")
                        correct += 1
                        checkStr = True
                    elif result != (subtract - subtractFrom):
                        print("Wrong.")
                        wrong += 1
                        checkStr = True
                        print("Result:", substract - substractFrom)
                elif any(str.isdigit(c) for c in result) == False:
                    if result == "exit":
                        WorkState = "exit"
                        checkStr = True
                        print("Correct answers: ", correct, ", Wrong answers:", wrong, ".")
                    else:
                        print("You typed in a text, not a number.")
