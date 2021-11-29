# SimpleX-Calculator

![SimpleX Logo](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/Simplex-loggo.PNG)

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

  *   The user should get a feedback when a wrong option is selected.

  *   If a user enters an incorrect number as input, the user should receive feedback.

  *   The user should be able to continue or not continue with carrying out more calculations.

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

I distributed the app's URL to my friends and family members in order for them to test the app's fundamental math features (laptops)

* All maths functions implemented are working perfectly.

  *   The user should be able to add two integers and receive the correct answer.

User inputs two numbers, the app performs the addition function and produces the correct result as seen in the screenshots below:
![Add Function](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/Addition-function.PNG)


  *   The user must be able to subtract two integers and arrive at the correct answer.

User inputs two numbers, the app performs the subtraction function and produces the correct result as seen in the screenshots below:
![Subtract Function](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/Subtract-function.PNG)

  *   The user must be able to multiply two integers and obtain the correct answer.

  *   The user must be able to divide two integers and come up with the correct answer.

  *   The user should be able to correctly compute the square root of an integer.

  *   The user should get a feedback when a wrong option is selected.

  *   If a user enters an incorrect number as input, the user should receive feedback.

  *   The user should be able to continue or not continue with carrying out more calculations.

__Bugs__

  * User were able to carry out just two (2) functions on the app, he/she will have to run the program again. This was fixed by removing the break statement which was initially in between the function written to prompt users to carry out calculations again.

  * When User gives empty input when selecing the calculation option, it does not raise any error. This was fixed using the "While True" loop which was used to indicate that the loop has to run until it breaks.

__Frameworks, Libraries and Programs Used__

* Git

  * The Gitpod terminal was used to commit to Git and push to GitHub, which was utilized for version control.

* GitHub

  * After the project's code was pushed from Git, it was stored on GitHub.

__Validator Testing__

* PEP8 Online

The code was validated using the PEP8 online validation tool to verify there were no syntax problems or inappropriate code indentation. [PEP8online](http://pep8online.com/)

   * There were no errors were returned when passing through the official PEP8 Validator.

![Validator result](https://github.com/RH-devs/SimpleX-Calcuator/blob/main/assets/images/PEP8-VALIDATION.PNG)


## Technologies Used

__Languages Used__

* Python

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

- The Following steps below were used to deploy this project to Heroku:

 * To begin, a new line character must be appended to the end of the input text and saved in order for the input method to   operate correctly in the deployed platform Heroku; otherwise, the text will not appear in the terminal.

 * In scenarios when the project has many dependencies, such as gspread and google-auth, construct a list of prerequisites that the project need in order to execute. These dependencies must also be installed on Heroku, and they must be included to the requirements.txt file. For, this project, there is no content in the requirements.txt file. It wasn't utilized because it wasn't required for this project, but it was left there because it is necessary for Heroku to function properly.

 * Go to Heroku's website and sign up for an account by clicking the link below: https://id.heroku.com/login Fill out the form with your information, including your First Name, Last Name, Email Address, Role (for example, "student"), Country (for example, location), and Language (for example, Python). If you're sure you're not a robot, click the "Create free account" button at the bottom of the page.

 * Open the confirmation email given to the email address you used to register with Heroku. To confirm, click the link provided, which will lead you to a new page where you may establish a password, then click the "Set password and Login button." A welcome message appears, so click the "Click here to proceed" button and accept the terms.

 * Click the "Create new app" button on the Heroku dashboard, give your app a unique name, pick your location, and then click the "Create app" button.
 
 * Scroll down to the 'Config Vars' section and click on the 'Reveal Config Vars' button after clicking on the "Settings" tab at the top of the page. Type the word "PORT" in all capital letters in the 'KEY' area, and '8000' in the value field, then click the 'Add' button.

 * After that, scroll down to the 'Buildpacks' area and click the "Add buildpack" button, then pick "Python" as the first buildpack required and click the "Save changes" button. Click the "Add buildpack" button once more, this time selecting "node.js" as the second buildpack required, and then clicking the "Save changes" button. Ensure that the buildpacks are in the correct sequence, with Python on top and node.js below, or click & drag them into place.

 * Select GitHub as the deployment option from the "Deploy" tab at the top of the page, then scroll down and select the "Connect to GitHub" button.

 * Search for your repository name by putting it into the search box and clicking "Search," then click "Connect" to connect your Heroku app to your GitHub repository code.

 * Next, scroll down to the "Automatic Deploys" section and click the "Enable Automatic Deploys" button to have Heroku rebuild the app whenever a new modification is uploaded to your GitHub source.

 * Finally, you'll get a notification that reads "Your app was successfully published," along with a 'View' button that will take you to the deployed URL.

 * The program begins (i.e. runs) automatically on the deployed site, but you may restart it (i.e. run it again) by clicking the "RUN PROGRAM" button at the top of the page.


__Cloning (Local Deployment)__

* The repository may be cloned (i.e. copied onto their system and executed locally from there) to run this application locally by following the procedures below:
In your terminal, type the following command:[Git clone](https://github.com/RH-devs/SimpleX-Calcuator.git)

* After cloning the project, use this command to install the packages from the requirements.txt file: 'Pip3 freeze > requirements.txt'. However, despite the fact that this project does not include any external Python packages, it is still required (i.e. the requirements.txt file) for the Heroku setup.

* The live link can be found here – [SimpleX Calculator](https://simplex-calculator.herokuapp.com/)
* The GitHub Repository can be found here - [SimpleX Calculator](https://github.com/RH-devs/SimpleX-Calculator)

## Credits

__Content__

* The app logo image “SimpleX-Calculator” was taken from Google while the app name was formed by me.

* I followed an online tutorial video from YouTube by Learn Code, You can find video tutorial here [Learn Code](https://youtu.be/61DrWY_ao4A).

* The Flake8Rules resource was utilized to resolve issues with a indentation.

* I used the Love-sandwiches (Essential python project) videos. Though the code has some similarities, i was able to apply my own metrics to the building the functions.

* I also checked Stackover flow to resolve an issue with looping [Stackoverflow](https://stackoverflow.com/questions/68109027/python-using-for-loop-in-def-function)


## Acknowledgement

 * Code Institute on the walkthrough python essential project.

 * My mentor Brian Macharia for pointing out errors made and assisting in resolving it.

 * Learn Code tutorial video on YouTube for helpful resources.

 * Stackoverflow and flake8rules resources.
