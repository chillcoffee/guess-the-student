import html
import random


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        #q_text = html.unescape(self.current_question.text)
        q_image = self.current_question.image
        print(q_image)
        return q_image

    def printChoices(self, choices):
        random.shuffle(choices)
        correct_letter = ""
        print(f"A. {choices[0]}\nB. {choices[1]}\nC. {choices[2]}\nD. {choices[3]}")
        for i in range(0,4):
            if choices[i] == self.current_question.answer:
                correct_letter = chr(65+i)
        return correct_letter

    def show_question(self, ):
        """
            showing question for multiple choice questions
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)

        print(f"{self.question_number}. {q_text}")

        choices_list = self.current_question.choices
        correct_letter = self.printChoices(choices_list)
        user_answer = input("\nYour answer: ")
        self.check_answerInput(user_answer, correct_letter)



    def check_answerInput(self, user_answer, correct_letter):
        correct_answer = correct_letter
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

