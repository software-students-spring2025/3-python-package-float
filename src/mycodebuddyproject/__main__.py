"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""
import fun_facts as fun_fact
from study_timer import StudyTimer

def main():
    """
    Here is where we will call our functions
    """
    try:
        function = int(input("What do you need help with? \n1. Debugging Tip\n2. Python Fun Fact\n3. Help Resources\n4. Study Timer\n(enter a number between 1-3): "))
        while (function < 1 or function > 4):
            function = int(input("Not a valid category. Please choose a number between 1-3: "))
        try:
            if (function == 1):
                ###call debugging tips function here
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
                ###call help function here
                exit()
            
            elif function == 4:
            # study timer menu
                timer = StudyTimer()
                while True:
                    action = int(input("\nStudy Timer Options:\n1. Start Studying\n2. Stop/Break\n3. Resume\n4. Exit Timer\nChoose an option (1-4): "))
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
                    else:
                        print("Not a valid type. Please choose a number between 1-4.")


        except ValueError as e:
                print(e)
    except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()