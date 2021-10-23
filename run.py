def select_operator():
    """
    User input is requested for operator selection,
    and if an incorrect option is made, the user is
    given relevant feedback.
    """

    global option
    option = input(
                 "The functions below will help carry out your calculation:\n"
                 "1. Addition\n"
                 "2. Subtraction\n"
                 "3. Multiply\n"
                 "4. Division\n"
                 "5. Square root\n"
                 "6. Exit\n")
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
        print("Calculation completed Successfully.\n")
        return result
    else:
        num1 = number_entry("Enter first number")
        num2 = number_entry("Enter second number")
        my_option = option
        if my_option == "1":
            print("Currently adding numbers...\n")
            result = num1 + num2
            return result


def number_entry(pos):
    """
    This function asks for numerical inputs from the user, manages errors,
    and provides relevant feedback to the user on the cause of the issue
    and how to resolve it.
    """
    while True:
        try:
            num = float(input(f"Enter {pos} number:\n"))
            return num
        except ValueError:
            print("Invalid entry, Please try again!:\n")


"""
Accept user name and displays a personalised welcome message
to the user.
"""
your_name = input("(Optional) Please Enter your name: \n")
print(f"Welcome {your_name} to the SimpleX")
answer = numeric_operation()
print(f"The answer to your calculation is {answer}")
