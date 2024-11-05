Math Quiz Game

Overview

This is a simple math quiz game implemented in Python, where users can answer random math problems to test their basic arithmetic skills. The program generates random numbers, operators, and math problems for the user to solve, and gives feedback on whether the answer is correct.

The project has been cleaned up and structured for better maintainability. Additionally, the repository has been made pip installable.

Features

Generates random math problems with basic operators (+, -, *)
Tracks the user’s score
Unit tests to ensure the core functions are working correctly
Pip installable as a Python package
Improvements & Clean-up

Code Refactoring: Improved readability and structure of the code.
File Organization: Structured the project for better scalability with proper directory structure.
Added Unit Tests: Introduced unit tests using Python’s unittest module to validate the random number generation, operator selection, and problem creation logic.
Added setup.py: Created a setup.py file to make the project pip installable directly from GitHub.
Created __init__.py: Included the __init__.py file to ensure the project is recognized as a Python package.
Licensing: Applied the Apache License 2.0 to the project for open-source usage.
Installation

To install this project locally, follow the steps below:

Clone the repository:
bash
Copy code
git clone https://github.com/prashanthgadwala/dsss_homework_2.git
Navigate to the project directory:
bash
Copy code
cd dsss_homework_2
Install the package using pip:
bash
Copy code
pip install git+https://github.com/prashanthgadwala/dsss_homework_2.git
Usage

Once the package is installed, you can run the math quiz game from the command line:

bash
Copy code
python3 -m math_quiz.math_quiz
You will be prompted with random math problems to solve. Answer the questions to accumulate your score.

Tests

The project includes unit tests for the core functions (generate_random_number, generate_random_operator, create_math_problem). To run the tests, use:

bash
Copy code
python3 -m unittest discover
This will run all the tests and ensure that the functions behave as expected.

Project Structure

arduino
Copy code
│ .gitignore
│ LICENSE
│ README.md
│ requirements.txt
│ setup.py
└─math_quiz
   ├── __init__.py
   ├── math_quiz.py
   └── tests_math_quiz.py
License

This project is licensed under the Apache License 2.0.

Contributing

If you would like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

Key Sections:
Overview: A brief description of what the project does.
Features: What makes the project useful or interesting.
Improvements & Clean-up: The work you did to improve and clean up the provided code.
Installation: Instructions on how to install the project using GitHub as a remote repository.
Usage: How to run the game or use the package.
Tests: Information on the unit tests and how to run them.
Project Structure: Shows the organization of files and directories.
License: Information on the licensing of the project.
Contributing: How others can contribute to the project.
Steps to follow:
Open a text editor and create a new file named README.md in your repository's root folder.
Paste the template above into the file.
Edit the sections that require personalization, such as the project name, description, and any other specifics of your implementation.
Commit and push the README.md file to your GitHub repository to share with others.
