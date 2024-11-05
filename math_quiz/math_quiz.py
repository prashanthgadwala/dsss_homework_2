import random

def generate_random_number(min_value, max_value):
    """
    Generate a random float between min_value and max_value.
    
    Args:
        min_value (float): The minimum value.
        max_value (float): The maximum value.
    
    Returns:
        float: A random float between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Generate a random operator from the list ['+', '-', '*'].
    
    Returns:
        str: A random operator.
    """
    return random.choice(['+', '-', '*'])

def create_math_problem(num1, num2, operator):
    """
    Create a math problem and calculate the answer.
    
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operator (str): The operator ('+', '-', '*').
    
    Returns:
        tuple: A tuple containing the problem string and the answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
    """
    Run the math quiz game.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 6)
        operator = generate_random_operator()

        problem, correct_answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = input("Your answer: ")
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()