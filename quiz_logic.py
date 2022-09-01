class QuizLogic:

    def __init__(self, question_list):
        self.question_number = 0
        self.list = question_list

    def still_has_questions(self):
        return len(self.list) > self.question_number

    def next_question(self):
        current_question = self.list[self.question_number].text
        self.question_number += 1
        input(f'Q.{self.question_number}: {current_question} (True/False)?')
