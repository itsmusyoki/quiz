class QuizBrain:
    def __init__(self, question_list):
        # qno and qlist
        self.q_list = question_list
        self.q_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.q_number < len(self.q_list)
    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_choice = input(f'Q.{self.q_number}: {current_question.text}(True/False)?: ')
        self.check_answer(user_choice, current_question.answer)


    def check_answer(self, user_choice, correct_answer):

        if user_choice.lower() == correct_answer.lower():
            print("that's correct!!")
            self.score += 1
            print(f"you score is {self.score}/{self.q_number}")

        else:
            print(f"the correct answer is {correct_answer}")

