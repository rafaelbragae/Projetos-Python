class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_line = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_line)

    def new_question(self):
        current = self.question_line[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current.text} (True/False):")
        self.check_answer(user_answer,current)

    def check_answer(self, answer, current):
        if answer == current.answer:
            self.score += 1
            print("Your answer is right")
        else:
            print("Your answer is wrong")
        print(f"The correct answer is: {current.answer}\nYour current score is: {self.score}/{self.question_number}\n")
