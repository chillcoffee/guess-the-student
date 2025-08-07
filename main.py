from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
from name import Name
import random
import subprocess
import os
from stat import S_IREAD

question_bank = []
for question in question_data:
    question_text = question["lastname"]
    question_answer = question["firstname"]
    new_question = Question(question_text, question_answer, [])
    question_bank.append(new_question)

random.shuffle(question_bank)
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

#saving to file
# subprocess.check_call(["attrib", "+H", "result.txt"])
# os.chmod("result.txt", S_IREAD)
# input("Press any key to exit...")
