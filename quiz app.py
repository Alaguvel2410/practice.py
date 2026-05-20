import tkinter as tk
from tkinter import messagebox

# Sample Questions
QUESTIONS = [
    {
        "question": "What does CPU stand for?",
        "options": ["central processing unit", "computer processing unit", "central performance unit", "computer performance unit"],
        "correct_option": 1
    },
    {
        "question": "Which programming language is known for its simplicity and reliability?",
        "options": ["python", "java", "c++", "javascript"],
        "correct_option": 1
    },
    {
        "question": "What is the primary function of the operating system?",
        "options": ["to manage hardware resources", "to provide a platform for running applications", "to manage user account", "to manage network connection"],
        "correct_option": 1
    },
    {
        "question": "Which data management system is widely used for web applications?",
        "options": ["mysql", "postgresql", "microsoft", "oracle"],
        "correct_option": 1
    },
    {
        "question": "What is the term for a network attack that involves sending a large amount of traffic to a website?",
        "options": ["phishing", "malware", "denial of service (dos)", "man in the middle"],
        "correct_option": 3
    },
    {
        "question": "Which programming paradigm is based on the concept of objects and classes?",
        "options": ["object-oriented programming (OOP)", "functional", "imperative", "declarative programming"],
        "correct_option": 1
    },
    {
        "question": "What is the term for a small program that runs on a web page?",
        "options": ["applet", "script", "program", "application"],
        "correct_option": 1
    },
    {
        "question": "Which web development framework is widely used for building dynamic web applications?",
        "options": ["react", "angular", "vue.js", "django"],
        "correct_option": 4
    },
    {
        "question": "What is the term for a type of malware that demands payment in exchange for restoring access to data?",
        "options": ["ransomware", "trojan", "virus", "worm"],
        "correct_option": 1
    },
    {
        "question": "Which cloud computing service provides a platform for building and deploying web applications?",
        "options": ["amazon web services", "microsoft azure", "google cloud platform", "heroku"],
        "correct_option": 1
    },
    {
        "question": "What is the term for a type of network attack that involves intercepting and altering communication between two parties?",
        "options": ["man in the middle", "denial of service", "phishing", "malware"],
        "correct_option": 1
    },
    {
        "question": "Which programming language is widely used for building operating systems and embedded systems?",
        "options": ["c", "c++", "java", "python"],
        "correct_option": 1
    },
    {
        "question": "What is the term for a type of database that stores data in a structured format using tables and rows?",
        "options": ["relational database", "noSQL database", "graph", "object-oriented database"],
        "correct_option": 1
    },
    {
        "question": "Which web development framework is widely used for building static websites and web applications?",
        "options": ["ruby on rails", "django", "flask", "jekyll"],
        "correct_option": 4
    },
    {
        "question": "What is the term for malware that disguises itself as legitimate software?",
        "options": ["trojan", "virus", "worm", "ransomware"],
        "correct_option": 1
    },
    {
        "question": "Which cloud computing service provides a platform for building and deploying machine learning models?",
        "options": ["amazon web services", "microsoft azure", "google cloud platform", "IBM Watson"],
        "correct_option": 1
    },
    {
        "question": "What is the term for a type of network attack that involves sending a large amount of traffic to a network device?",
        "options": ["denial of service", "distributed denial of service", "man in the middle", "phishing"],
        "correct_option": 2
    },
    {
        "question": "Which programming language is widely used for building web applications using the Ruby on Rails framework?",
        "options": ["Ruby", "python", "java", "javascript"],
        "correct_option": 1
    },
    {
        "question": "What is the term for a type of database that stores data in a flexible, schema-less format?",
        "options": ["relational database", "NoSQL database", "graph database", "object-oriented database"],
        "correct_option": 2
    },
    {
        "question": "Which cloud computing service provides a platform for building and deploying serverless applications?",
        "options": ["amazon web services", "microsoft azure", "google cloud platform", "cloud Foundry"],
        "correct_option": 1
    }
]

# Quiz App class
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("900x700")
        self.root.configure(bg="#87ceeb")
        self.questions = QUESTIONS
        self.current_index = 0
        self.score = 0
        self.selected_answer = {}
        self.setup_ui()

    def setup_ui(self):
        # Header label
        self.header_label = tk.Label(self.root, text="FACTS WITH QUIZ", font=("Arial", 32, "bold"), bg="#4682b4", fg="white")
        self.header_label.pack(fill="x", pady=20)

        # Question label
        self.question_label = tk.Label(self.root, text="", font=("Arial", 24, "bold"), bg="#87ceeb", wraplength=850, justify="center")
        self.question_label.pack(pady=40)

        # Options
        self.options = tk.IntVar()
        self.options_frame = tk.Frame(self.root, bg="#87ceeb")
        self.options_frame.pack(pady=20)
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.options_frame, text="", variable=self.options, value=i + 1,
                font=("Arial", 20), bg="#87ceeb", fg="black", activebackground="dark red",
                activeforeground="white", wraplength=800, anchor="center"
            )
            rb.pack(anchor='center', pady=10)
            self.radio_buttons.append(rb)

        # Navigation frame
        self.navigation_frame = tk.Frame(self.root, bg="#87ceeb")
        self.navigation_frame.pack(pady=30)

        self.previous_button = tk.Button(self.navigation_frame, text="Previous", command=self.previous_question, bg="#ffb6c1", fg="black", font=("Arial", 16, "bold"), width=12)
        self.previous_button.grid(row=0, column=0, padx=20)

        self.next_button = tk.Button(self.navigation_frame, text="Next", command=self.next_question, bg="#98fb98", fg="black", font=("Arial", 16, "bold"), width=12)
        self.next_button.grid(row=0, column=1, padx=20)

        self.submit_button = tk.Button(self.navigation_frame, text="Submit", command=self.submit_quiz, bg="#1e90ff", fg="white", font=("Arial", 16, "bold"), width=12)
        self.submit_button.grid(row=0, column=2, padx=20)

        self.cancel_button = tk.Button(self.root, text="Cancel", command=self.root.quit, bg="red", fg="white", font=("Arial", 16, "bold"), width=15)
        self.cancel_button.pack(pady=20)

        self.display_question()

    def display_question(self):
        question = self.questions[self.current_index]
        self.question_label.config(text=f"Q{self.current_index + 1}: {question['question']}")
        for i, rb in enumerate(self.radio_buttons):
            rb.config(text=question['options'][i])
        self.options.set(self.selected_answer.get(self.current_index, 0))

    def save_answer(self):
        self.selected_answer[self.current_index] = self.options.get()

    def next_question(self):
        self.save_answer()
        if self.current_index < len(self.questions) - 1:
            self.current_index += 1
            self.display_question()
        else:
            messagebox.showinfo("End", "This is the last question.")

    def previous_question(self):
        self.save_answer()
        if self.current_index > 0:
            self.current_index -= 1
            self.display_question()
        else:
            messagebox.showinfo("Start", "This is the first question.")

    def submit_quiz(self):
        self.save_answer()
        for i, question in enumerate(self.questions):
            if self.selected_answer.get(i) == question['correct_option']:
                self.score += 1
        self.show_score()

    def show_score(self):
        score_window = tk.Toplevel(self.root)
        score_window.title("Quiz Results")
        score_window.geometry("500x300")
        score_window.configure(bg="#ffebcd")

        tk.Label(score_window, text="Quiz Completed!", font=("Arial", 24, "bold"), bg="#ffebcd", fg="#4682b4").pack(pady=30)
        tk.Label(score_window, text=f"Your Score: {self.score}/{len(self.questions)}", font=("Arial", 22), bg="#ffebcd", fg="black").pack(pady=20)
        tk.Button(score_window, text="Close", command=self.root.quit, bg="#ff4500", fg="white", font=("Arial", 16, "bold")).pack(pady=30)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
