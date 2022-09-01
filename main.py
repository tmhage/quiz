from data import question_data
from question_model import Question
from quiz_logic import QuizLogic

question_bank = []
for question in question_data:
    q_question = question['text']
    q_answer = question['answer']
    new_question = Question(q_question, q_answer)
    question_bank.append(new_question)

quiz = QuizLogic(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('The quiz is finished.')
print(f'Your final score is: {quiz.score}/{quiz.question_number}')