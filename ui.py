from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.tf_score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.eval('tk::PlaceWindow . center')

        self.window.title("❤️❤️❤️Guess your Student❤️❤️❤️")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label_score = Label(text="Score: ", fg="WHITE", bg=THEME_COLOR, font=("Arial", 14, "bold"))
        self.label_score.grid(row=0, column=1, pady=20)


        self.photo = PhotoImage(file="images/scientists/"+'Gates, Bill.png')
        self.canvas = Canvas(width=300, height=250, bg="WHITE")
        self.image_square = self.canvas.create_image(300/2, 250/2, image=self.photo)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)


#-----------------------your answer--------------------------------------------------------#
        self.label_question = Label(text="Who is this? ", fg="WHITE", bg=THEME_COLOR, font=("Monotype Corsiva", 18, "bold"))
        self.label_question.grid(row=2, column=0, columnspan=2, pady=10)

        self.entry_answer = Entry(bg="WHITE", fg=THEME_COLOR, font=("Monotype Corsiva", 18, "bold"))
        self.entry_answer.grid(row=3, column=0, columnspan=2, pady=10)

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.button_false = Button(image=false_img, highlightthickness=0, command=self.click_false, )
        self.button_true = Button(image=true_img, highlightthickness=0, command=self.click_true, )

        self.button_false.grid(row=4, column=1, pady=20)
        self.button_true.grid(row=4, column=0, pady=20)

        self.get_next_question()
        self.window.resizable(False, False)
        width = 350
        height = 650
        
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        self.window.mainloop()

    def get_next_question(self):
        self.label_score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_image = self.quiz.next_question()
            self.photo = PhotoImage(file="images/scientists/" + q_image)
            # self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.itemconfig(self.image_square, image=self.photo)
        else:
            self.tf_score = self.quiz.score
            with open("result.txt", mode="a") as file:
                file.write(f"\n\nTest I. True or False\nScore: {self.quiz.score}\n")
            #show final score here if there is
            self.canvas.create_text(150, 50, text=f"{self.quiz.score}/{len(self.quiz.question_list)}", font=("Monotype Corsiva", 24, "bold"))
            self.end_photo = PhotoImage(file="images/end_photo.png")
            self.canvas.itemconfig(self.image_square, image=self.end_photo)
            self.canvas.config(bg="white")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def click_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def click_true(self):
        user_answer = self.entry_answer.get().strip()
        self.give_feedback(self.quiz.check_answer(user_answer))
        self.entry_answer.delete(0, "end")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
