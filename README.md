# SimpleX-Calculator

![SimpleX Logo](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/Simplex-logo.PNG)

This project uses the Python programming language to construct a text-based calculator with limited functionality that allows a user to enter one or two values depending on the operation to be performed, and the code does the operation and delivers the appropriate result.   Users basically follow the text-based instructions given on the terminal, and if the steps are followed in order, the right result is printed on the terminal. Because Python is a back-end language, there is no graphical user interface (GUI) accessible to interact with the calculator. 

![Device Mockup](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/simplex-mockup-images.png)

## UX

__SimpleX-Calculator__

The app was created with easy functionalities for anyone to carry out numerical functions in their daily activities. The users will be able to the calculate basic maths functions and it is clear enough for any individual of age (both old and young) to access it without limitations.

## Flowchart
The flowchart was created using the Lucid app and it captures the flow of operation created for the Calculator.
 
 * See flowchart below:

 ![Flow Chart](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/SIMPLEX-FLOWCHART.PNG)

**User Objectives** 

  *   The user should be able to add two integers and receive the correct answer.

  *   The user must be able to subtract two integers and arrive at the correct answer.

  *   The user must be able to multiply two integers and obtain the correct answer.

  *   The user must be able to divide two integers and come up with the correct answer.

  *   The user should be able to correctly compute the square root of an integer.

  *   If a user enters an incorrect number as input, the user should receive feedback.

## Features
 This section shows all existing features created to make the calculator functional.

__Existing Features__
* Option '1' represents Addition ('+') operator for the sum of two numbers.

![Add Function](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/Addition-function.PNG)

* Option '2' represents Subtraction ('-') operator for the difference between two numbers.

![Subtract Function](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/Subtract-function.PNG)

* Option '3' represents Multiply ('*') operator for the product of two numbers.

![Multiply Function](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/multiply-function.PNG)

* Option '4' represents Division ('/') operator to divide two numbers.

![Division Function](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/division-function.PNG)

* Option '5' for Square Root ('√') operator to retrieve the square root of a number.

![Division Function](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/squareroot-function.PNG)

* Option '6' for Exit.

![Exit Function](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/exit-function.PNG)

## Future Enhancements

__Adding more mathematical functions to the app__

* This feature will help users have choice of using the calculator to carry out other mathematical functions such as Modulo, Median, Mean, Exponent etc.  The impact of this will enhance user experience.

## Testing

I tested it in two dimensions for testing. The initial stage was to test the functions on the Gitpod terminal as they were being developed to ensure I was on track with applying them appropriately and that they worked.
This was the second level of testing after it was deployed to Heroku. I used a more formal structured approach and tested each function once more. I then ran through the tests for each device to ensure the app functioned properly.

__User level Testing__

I distributed the app's URL to my friends and family members in order for them to test the app's fundamental math features (mobiles, laptops, etc.)

* All maths functions implemented are working perfectly

* Website Responsiveness
  * Issue reported with footer contents not aligned on smaller screens was corrected by changing the display to flex.
  * Issue reported with Progress bar and Score conflicting with size on mobile screen was resolved by reducing the font-size.

*	Bugs

  * User is able to carry out just three (3) functions, he/she will have to run the program again.

__Validator Testing__
* PEP8 Online

The code was validated using the PEP8 online validation tool to verify there were no syntax problems or inappropriate code indentation.

   * There were no errors were returned when passing through the official PEP8 Validator.

![Validator result](https://github.com/RH-devs/Dushlan-spraoi/blob/main/assets/images/PEP8-VALIDATION.PNG)

