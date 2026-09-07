class InvalidAnswerError(Exception):
    pass

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question["question"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")

    def get_answer(self):
        answer = input("Enter your answer (1-4): ")
        if answer not in ["1", "2", "3", "4"]:
            raise InvalidAnswerError("Invalid answer. Choose between 1 and 4")
        return int(answer)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            return True
        return False

    def calculate_score(self):
        return (self.score / len(self.questions)) * 100

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

quiz = Quiz(questions)

for question in quiz.questions:
    quiz.display_question(question)
    try:
        answer = quiz.get_answer()
        if quiz.check_answer(answer, question["answer"]):
            quiz.score += 1
            print("Correct")
        else:
            print("Wrong")
    except InvalidAnswerError as e:
        print(e)

total_questions = len(quiz.questions)
correct = quiz.score
wrong = total_questions - correct
score = quiz.calculate_score()

print(f"Total Questions: {total_questions}")
print(f"Correct: {correct}")
print(f"Wrong: {wrong}")
print(f"Score: {score}%")