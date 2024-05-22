from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# a list of question objects
question_bank = []
# make question objects from the list of dictionaries
for question in question_data:
    # {"text": "A slug's blood is green.", "answer": "True"}
    q_text = question["text"]
    q_answer = question["answer"]
    q_object = Question(q_text, q_answer)
    question_bank.append(q_object)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
