class QuizLogic:

    def __init__(self, question_list):
        self.question_number = 0
        self.list = question_list

    def next_question(self):
        number = self.question_number
        question = self.list[number].text
        input(f'Q.{number + 1}: {question} (True/False)?')
