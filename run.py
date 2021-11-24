import sys


def select_operator():
    """
    User input is requested for operator selection,
    and if an incorrect option is made, the user is
    given relevant feedback.
    """

    global option
    while True:
        option = input(
                 "The functions below will help carry out your calculation:\n"
                 "Select your preferred option:\n"
                 "1. Addition\n"
                 "2. Subtraction\n"
                 "3. Multiply\n"
                 "4. Division\n"
                 "5. Square root\n"
                 "6. Exit\n")

        option = option.strip()

        if option not in {'1', '2', '3', '4', '5', '6'}:
            print("Invalid selector. Please select options between 1 and 6")

        else:
            break

    if option == '6':
        sys.exit(0)

    return option


def numeric_operation():
    """
    Based on the user's selection, performs the required computation
    and returns the result to the calling code.
    """
    select_operator()
    NUM_CONSTANT = 0.5
    if option == "5":
        print("Currently working on Square Root...\n")
        sqrt_num = number_entry("1")
        result = sqrt_num ** NUM_CONSTANT
        print("Calculation Successfully Done.\n")
        return result
    else:
        num1 = number_entry("1st number")
        num2 = number_entry("2nd number")
        my_option = option
        if my_option == "1":
            print("Currently working on Addition function...\n")
            result = num1 + num2
            print("Calculation Successfully Done.\n")
            return result
        elif my_option == "2":
            print("Currently working on Subtract function...\n")
            result = num1 - num2
            print("Calculation Successfully Done.\n")
            return result
        elif my_option == "3":
            print("Currently working on Multiply function...\n")
            result = num1 * num2
            print("Calculation Successfully Done.\n")
            return result
        elif my_option == "4":
            print("Currently working on Division function...\n")
            try:
                if True:
                    result = num1 / num2
                    print("Calculation Successfully Done.\n")
                return result
            except ZeroDivisionError as err:
                print("Number can't be divided by 0")
        else:
            return " None, An invalid operator has been selected"


def number_entry(pos):
    """
    This function asks for numerical inputs from the user, manages errors,
    and provides relevant feedback to the user on the cause of the issue
    and how to resolve it.
    """
    while True:
        try:
            num = float(input(f"Enter {pos}:\n"))
            return num
        except ValueError:
            print("Invalid entry, Please try again!:\n")


def welcome():
    """
    Accept user name and displays a personalised welcome message
    to the user.
    """
    user_name = input("(Optional) Please input your name: \n")
    print(f"Welcome {user_name} to the SimpleX")
    answer = numeric_operation()
    print(f"The answer to your calculation is {answer}")


welcome()


def again():
    """
    If the user wishes to execute another action,
    the app will be repeated;
    if not, the app will display the final result and quit.
    """
    response = input("Do you want to carry out another Calculation y/n?\n")
    while response == "y" or response == "Y":
        current_answer = numeric_operation()
        print(f"The result of your calculation is {current_answer}\n")
        response = input("Do you want to carry out another Calculation y/n?\n")
    else:
        print(f"We appreciate you for using SimpleX calculator. Goodbye!")


again()


