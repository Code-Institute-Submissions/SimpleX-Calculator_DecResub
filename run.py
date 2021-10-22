# Simple text-based Calculator

def select_operator():
    """
    User input is requested for operator selection,
    and if an incorrect option is made, the user is
    given relevant feedback.
    """
    while True:
        print("The functions below will help carry out your basic calculations.")
        print("1 for Multiply")
        print("2 for Addition")
        print("3 for Subtraction")
        print("4 for Modulo")
        print("5 for Division")
        print("6 for Power(Exponent)")

    option.str = input("Please select an operation to perform your calculation:")
    
    select_operator = option.str("")

    if calculating_operator(option.str):
        print(f"You selected {option}")


def calculating_operator():
    """
    Based on the user's selection,it performs the appropriate computation
    and returns the result to the calling code.
    """
    calculating_operator()
  


def number_entry(pos):
    """
    This function asks for numerical inputs from the user, manages errors,
    and provides relevant feedback to the user on the cause of the issue
    and how to resolve it.
    """
    try:
        num = float(input(f"Enter {pos} number:\n"))
        return num
    except ValueError:
        print("Invalid entry - NOT a number. \n"
                  "Please try again!")


"""
Receives the user name and displays a welcome message
in relation to the user.
"""
user_name = input("(Optional) Input your name: \n")
print(f"Welcome {user_name} to SimpleX Calculator")
answer = calculating_operator()
print(f"The Last Result of your calculation is {answer}")
