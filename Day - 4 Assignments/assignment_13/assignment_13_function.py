class InvalidAnswerError(Exception):
    pass

def display_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")

def get_answer():
    answer = input("Enter your answer (1-4): ")
    if answer not in ["1", "2", "3", "4"]:
        raise InvalidAnswerError("Invalid answer. Choose between 1 and 4")
    return int(answer)

def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return True
    return False

def calculate_score(correct, total):
    return (correct / total) * 100

questions = [
    {
        "question": "What is Python?",
        "options": ["Language", "Database", "OS", "Browser"],
        "answer": 1
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["func", "def", "function", "define"],
        "answer": 2
    }
]

score = 0

for question in questions:
    display_question(question)
    try:
        answer = get_answer()
        if check_answer(answer, question["answer"]):
            score += 1
            print("Correct")
        else:
            print("Wrong")
    except InvalidAnswerError as e:
        print(e)

total_questions = len(questions)
correct = score
wrong = total_questions - correct
percentage = calculate_score(correct, total_questions)

print(f"Total Questions: {total_questions}")
print(f"Correct: {correct}")
print(f"Wrong: {wrong}")
print(f"Score: {percentage}%")