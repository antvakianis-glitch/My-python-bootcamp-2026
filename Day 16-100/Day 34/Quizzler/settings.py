from tkinter import *
from tkinter import ttk

BACKGROUND_COLOR = "#375362"

class QuizSettings:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz Settings")
        self.window.configure(padx=40,pady=40,background=BACKGROUND_COLOR)

        self.categories = {
            "General Knowledge": 9,
            "Books": 10,
            "Film": 11,
            "Music": 12,
            "Science & Nature": 17,
            "Computers": 18,
            "Mathematics": 19,
            "Sports": 21,
            "Geography": 22,
            "History": 23,
            "Animals": 27,
        }
        self.setup_ui()
        self.parameters = None

    def setup_ui(self):
        self.label_title = Label(self.window, text="🎯 Quiz Settings",font=("Arial", 24, "bold"),bg=BACKGROUND_COLOR,fg="white")
        self.label_title.grid(column=0, row=0, columnspan=2, pady=20)

        self.label_amount = Label(self.window,text="Questions:",font=("Arial", 12),bg=BACKGROUND_COLOR,fg="white")
        self.label_amount.grid(column=0, row=1, sticky="e", pady=20)

        self.amount_var = StringVar(value="10")
        self.amount_box = ttk.Combobox(self.window,textvariable=self.amount_var,values=["5","10","15","20"],state="readonly",font=("Arial", 12),)
        self.amount_box.grid(column=1, row=1, pady=10)

        self.category_text = Label(self.window,text="Category:",font=("Arial", 12),bg=BACKGROUND_COLOR,fg="white")
        self.category_text.grid(column=0, row=2, sticky="e", padx=10, pady=10)

        self.category_var = StringVar(value="Computers")
        self.category_box = ttk.Combobox(self.window,textvariable=self.category_var,values=list(self.categories.keys()),state="readonly",width=18)
        self.category_box.grid(column=1, row=2, pady=10)

        self.difficulty_text = Label(self.window, text="Category:", font=("Arial", 12), bg=BACKGROUND_COLOR, fg="white")
        self.difficulty_text.grid(column=0, row=3, sticky="e", padx=10, pady=10)

        self.difficulty_var = StringVar(value="medium")
        self.difficulty_box = ttk.Combobox(self.window, textvariable=self.difficulty_var,
                                         values=["easy", "medium", "hard"], state="readonly", width=18)
        self.difficulty_box.grid(column=1, row=3, pady=10)

        self.start_button = Button(self.window,text="Start Quiz",command=self.start_quiz,bg="#4CAF50",
            fg="white",
            font=("Arial", 14, "bold"),
            padx=30,
            pady=10)
        self.start_button.grid(column=0, row=4,columnspan=2, pady=30)

    def start_quiz(self):
        category_id = self.categories[self.category_var.get()]

        self.parameters = {
            "amount": int(self.amount_var.get()),
            "type":"boolean",
            "category":category_id,
            "difficulty": self.difficulty_var.get(),
        }

        self.window.destroy()

    def get_parameters(self):
        self.window.mainloop()
        return self.parameters