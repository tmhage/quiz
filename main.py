from data import question_data
from question_model import Question

question_bank = []
for question in question_data:
    q_question = question['text']
    q_answer = question['answer']
    new_question = Question(q_question, q_answer)
    question_bank.append(new_question)