from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

import random

question_bank = []
for question in question_data:
    question_text = question["lastname"]
    question_answer = question["firstname"]
    question_image = question["image"]
    new_question = Question(question_text, question_answer, question_image)
    question_bank.append(new_question)

random.shuffle(question_bank)
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
