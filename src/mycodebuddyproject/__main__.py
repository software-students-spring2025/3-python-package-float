"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""
import fun_facts as fun_fact


def main():
    """
    Here is where we will call our functions
    """
    try:
        function = int(input("What do you need help with? \n1. Debugging Tip\n2. Python Fun Fact\n3. Help Resources\n(enter a number between 1-3): "))
        while (function < 1 or function > 3):
            function = int(input("Not a valid category. Please choose a number between 1-3: "))
        try:
            if (function == 1):
                ###call debugging tips function here
                exit()

            elif (function == 2):
                type = int(input("\nAvailable types: \n1. Features\n2. Libraries\n3. Trivia\n4. Performance\nChoose a type (enter a number between 1-4): "))
                while (type < 1 or type > 4):
                    type = int(input("Not a valid type. Please choose a number between 1-4: "))
                if (type == 1):
                    print(fun_fact.get("features"))
                    exit()
                elif (type == 2):
                    print(fun_fact.get("libraries"))
                    exit()
                elif (type == 3):
                    print(fun_fact.get("trivia"))
                    exit()
                elif (type == 4):
                    print(fun_fact.get("performance"))
                    exit()
                else:
                    print("Error executing program")
                    exit()

            elif (function == 3):
                ###call help function here
                exit()

        except ValueError as e:
                print(e)
    except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()