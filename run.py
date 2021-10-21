# Simple text-based Calculator

def select_operator():
    """
    User input is requested for operator selection,
    and if an incorrect option is made, the user is
    given relevant feedback.
    """
    global option
    option = input(
                   "Please select an operation to perform"
                   "your numerical activity: \n"
                   "1 for Multiply\n"
                   "2 for Addition\n"
                   "3 for Subtraction\n"
                   "4 for Modulo\n"
                   "5 for Division\n"
                   "6 for Power(Exponent)\n")
    return option
