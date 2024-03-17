# Day 17 project from 100 Days of Code: The Complete Python Pro Bootcamp course

question_data = [
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "Pointers were not used in the original C programming language; they were "
                 "added later on in C++.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "Linus Torvalds created Linux and Git.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The Python programming language gets its name from the British comedy group "
                 "Monty Python",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "Ada Lovelace is often considered the first computer programmer.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "RAM stands for Random Access Memory.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The programming language &quot;Python&quot; is based off a modified version "
                 "of &quot;JavaScript&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The Windows 7 operating system has six main editions.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The logo for Snapchat is a Bell.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The NVidia GTX 1080 gets its name because it can only render at a "
                 "1920x1080 screen resolution.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
     "correct_answer": "True", "incorrect_answers": ["False"]}
]



class Question:
    def __init__(self, question_t, question_a):
        self.text = question_t
        self.answer = question_a


class QuizBrain:
    def __init__(self, question_l):
        self.question_number = 0
        self.question_list = question_l
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_a, correct_a):
        if user_a.lower() == correct_a.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_a}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


question_bank = []

for element in question_data:
    question_text = element["question"]
    question_answer = element["correct_answer"]
    new_question = Question(question_t=question_text, question_a=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
