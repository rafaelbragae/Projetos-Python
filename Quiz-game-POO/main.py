from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.new_question()
print(f"You`ve completed the quiz.\nYour final score was: {quiz.score}/{quiz.question_number}")
