questions = {
    "What's the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "What is the color of the sun?": "Yellow"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"You got {score}/{len(questions)} correct.")
