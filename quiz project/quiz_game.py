# quiz_game.py

import random
import time
from input_utils import get_int_input, InvalidAnswerError
from question_generator import generate_question
from colorama import Fore, Style, init

init(autoreset=True)

score = 0
user = input(Fore.CYAN + "🎮 Enter your name to start the quiz: ")
quiz_start_time = time.time()

print(Fore.MAGENTA + f"\n👋 Welcome {user}! Get ready for the Square & Square Root Quiz!\n")
print(Fore.YELLOW + "-" * 50)

question_number = 1

while True:
    print(Fore.BLUE + f"\n📘 Question {question_number}")
    question, correct_answer = generate_question()
    print(Fore.WHITE + f"👉 {question}")
    question_start_time = time.time()

    try:
        answer = get_int_input(Fore.LIGHTGREEN_EX + "✍️  Your answer: ")
        question_end_time = time.time()
        time_taken = round(question_end_time - question_start_time, 2)

        if answer == correct_answer:
            score += 10
            print(Fore.GREEN + "✅ Correct!")
        else:
            score -= 5
            print(Fore.RED + f"❌ Wrong! The correct answer was {correct_answer}")

        print(Fore.CYAN + f"⏱ Time taken: {time_taken} seconds")
        print(Fore.LIGHTMAGENTA_EX + f"🎯 Score: {score}")

        if score >= 50:
            print(Fore.GREEN + f"\n🏆 Congratulations, {user}! You are the Winner!\n")
            break


    except InvalidAnswerError as e:
        print(Fore.RED + f"{e}")
        continue

    print(Fore.YELLOW + "-" * 50)
    choice = input(Fore.LIGHTWHITE_EX + "🤔 Do you want to continue the quiz? (yes/no): ").strip().lower()
    if choice != "yes":
        print(Fore.RED + "\n👋 Exiting... Looser 💔\n")
        break

    question_number += 1
