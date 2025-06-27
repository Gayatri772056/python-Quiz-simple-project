import random

def generate_question():
    question_type = random.choice(["square", "square_root"])

    if question_type == "square":
        number = random.randint(1, 100)
        question = f"What is the square of {number}?"
        answer = number * number
    else:
        root = random.randint(1, 100)
        perfect_square = root * root
        question = f"What is the square root of {perfect_square}?"
        answer = root

    return question, answer
