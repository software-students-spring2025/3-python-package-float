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
                timer = StudyTimer()
                timer.start(1)
            elif function == 5:
            # study timer menu
                timer = StudyTimer()
                while True:
                    command = input("Enter command (start, exit): ").strip().lower()
                    if command == "start":
                        timer = StudyTimer()
                        timer.start()
                        while timer.running or timer.paused:
                            sub_cmd = input("\nEnter timer command (pause, resume, cancel, turn off alarm): ").strip().lower()
                            if sub_cmd == "pause":
                                timer.pause()
                            elif sub_cmd == "resume":
                                timer.resume()
                            elif sub_cmd == "cancel":
                                timer.cancel()
                            elif sub_cmd == "turn off alarm":
                                if timer.completed == True:
                                    break
                                else:
                                    print("The alarm is not going off yet...")
                            # Check for completion in the main thread:
                            if timer.completed:
                                timer.completed = False
                                break
                    elif command == "exit":
                        print("Exiting MyCodeBuddy.")
                        break
                    else:
                        print("Unknown command. Please try again.")

        except ValueError as e:
            print(e)

    except ValueError as e:
        print(e)
       


if __name__ == "__main__":
    main()