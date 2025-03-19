"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""
import fun_facts as fun_fact
import get_debug_tips as debug
import get_help as help
from study_timer import StudyTimer

def main():
    """
    Here is where we will call our functions
    """
    try:
        function = int(input("What do you need help with? \n1. Debugging Tip\n2. Python Fun Fact\n3. Help Resources\n4. Study Timer\n(enter a number between 1-4): "))
        while (function < 1 or function > 4):
            function = int(input("Not a valid category. Please choose a number between 1-4: "))
        try:
            if (function == 1):
                type = int(input("\nAvailable types: \n1. Syntax\n2. Runtime\n3. Logic\nChoose a type (enter a number between 1-3): "))
                while (type < 1 or type > 3):
                    type = int(input("Not a valid type. Please choose a number between 1-3: "))
                if (type == 1):
                    print(debug.debug_tip("syntax"))
                    exit()
                elif (type == 2):
                    print(debug.debug_tip("runtime"))
                    exit()
                elif (type == 3):
                    print(debug.debug_tip("logic"))
                    exit()
                else:
                    print("Error executing program")
                    exit()

            elif (function == 2):
                # fun facts
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
                type = int(input("\nWhat language do you need help with? \n1. Python\n2. Javascript\n3. Java\n4. c#\n5. c++\n6. php\n7. ruby\n8. swift\n9. r\n10. sql\n11. kotlin\n12. typescript\n13. go\n14. rust\n15. scala\n16. dart\n17. perl\nChoose a type (enter a number between 1-17): "))
                while (type < 1 or type > 17):
                    type = int(input("Not a valid type. Please choose a number between 1-17: "))
                if (type == 1):
                    print(help.language_help("Python"))
                    exit()
                elif (type == 2):
                    print(help.language_help("Javascript"))
                    exit()
                elif (type == 3):
                    print(help.language_help("Java"))
                    exit()
                elif (type == 4):
                    print(help.language_help("c#"))
                    exit()
                if (type == 5):
                    print(help.language_help("c++"))
                    exit()
                elif (type == 6):
                    print(help.language_help("php"))
                    exit()
                elif (type == 7):
                    print(help.language_help("ruby"))
                    exit()
                elif (type == 8):
                    print(help.language_help("swift"))
                    exit()
                if (type == 9):
                    print(help.language_help("r"))
                    exit()
                elif (type == 10):
                    print(help.language_help("sql"))
                    exit()
                elif (type == 11):
                    print(help.language_help("kotlin"))
                    exit()
                elif (type == 12):
                    print(help.language_help("typescript"))
                    exit()
                if (type == 13):
                    print(help.language_help("go"))
                    exit()
                elif (type == 14):
                    print(help.language_help("rust"))
                    exit()
                elif (type == 15):
                    print(help.language_help("scala"))
                    exit()
                elif (type == 16):
                    print(help.language_help("dart"))
                    exit()
                elif (type == 17):
                    print(help.language_help("perl"))
                    exit()
                else:
                    print("Error executing program")
                    exit()
            
            elif function == 4:
                while True:
                    try:
                        function = int(input("\nChoose an option:\n1. Study Timer\n2. Exit\nChoose an option (1-2): "))
                        if function == 1:
                            timer = StudyTimer()
                            while True:
                                if timer.timer_expired:
                                    print("Study session has ended!")
                                    break
                                action = int(input("\nStudy Timer Options:\n1. Start Studying\n2. Stop/Break\n3. Resume\n4. Exit Timer\n5. Turn off alarm\nChoose an option (1-5): "))
                                if action == 1:
                                    timer.start()
                                elif action == 2:
                                    response = timer.stop()
                                    if response == "yes":
                                        print("Enjoy your break!")
                                elif action == 3:
                                    timer.resume()
                                elif action == 4:
                                    print("Exiting Study Timer.")
                                    break
                                elif action == 5:
                                    break
                                else:
                                    print("Not a valid type. Please choose a number between 1-5.")

                        elif function == 2:
                            print("Exiting the program.")
                            break
                        else:
                            print("Invalid option, please choose between 1 and 2.")
                    except ValueError:
                        print("Please enter a valid number.")
        except ValueError as e:
            print(e)

    except ValueError as e:
        print(e)
       


if __name__ == "__main__":
    main()