import tkinter as tk
import random


BG = "#f4f6fb"
SAMPLE_BG = "#eef2ff"
TYPING_BG = "#ffffff"
TEXT_COLOR = "#1f2937"
BORDER = "#d1d5db"
ACCENT = "#4f46e5"
ACCENT_DARK = "#4338ca"

timer_started = False
seconds = 60
timer_id = None

sample_texts = [
    "Learning to type fast is a skill that rewards patience. At the beginning, your fingers feel slow and clumsy, and every mistake seems to cost you precious time. But with a little practice each day, something changes. Your hands start to remember where every key is, and your eyes no longer need to check the keyboard. The secret is to focus on accuracy first and speed second. If you rush, you will make more errors, and fixing them takes longer than typing slowly and correctly. Try to keep a steady rhythm, like a drummer keeping the beat. Sit up straight, relax your shoulders, and keep your wrists in a comfortable position. Look at the screen instead of your hands, and let your fingers find the way. Some people practice for ten minutes every morning, while others type a few paragraphs before bed. Either way, small steps add up over time. After a few weeks, you may be surprised by how far you have come. What once felt difficult becomes natural, and typing turns into something you do without thinking at all.",

    "The quick brown fox jumps over the lazy dog, and then it runs across the quiet field toward the old farmhouse near the river. The morning sun is bright, the air is cool, and the grass is still wet from the rain that fell during the night. A small bird sits on the fence and watches the fox with curious eyes. In the distance, a tractor starts its engine and begins to move slowly along the dusty road. The farmer waves to his neighbor, who is carrying a basket of fresh apples from the orchard. Everything in the village seems calm and peaceful, as if time itself has decided to rest for a while. Children walk to school, laughing and talking about their plans for the weekend.",

    "Practice makes perfect, and small steps add up over time. Every programmer starts with simple lines of code that print a few words on the screen. Then come variables, loops, and functions, and slowly the pieces begin to fit together. You will make mistakes along the way, and that is perfectly normal. Each error message is a clue that helps you understand how the computer thinks. Do not be afraid to experiment, to break things, and to fix them again. Build small projects that you enjoy, and share them with friends who can give you honest feedback. Read the code of others, ask questions when you are stuck, and take breaks when your mind feels tired. One day you will look back and realize how much you have learned, and how far you have traveled.",
]


def load_sample():
    sample_entry.config(state="normal")
    sample_entry.delete("1.0", "end")
    sample_entry.insert("1.0", random.choice(sample_texts))
    sample_entry.config(state="disabled")


def start_timer(event):
    global timer_started

    if not timer_started:
        timer_started = True
        update_timer()


def update_timer():
    global seconds
    global timer_id
    if seconds > 0:
        timer_id = window.after(1000, update_timer)
        seconds -= 1
        timer_label.config(text=f"Time: {seconds} seconds")
    else:
        my_entry.config(state="disabled")
        original = sample_entry.get("1.0", "end")
        typed = my_entry.get("1.0", "end")
        calculate_wpm(original, typed)


def restart_timer():
    global seconds
    global timer_started
    global timer_id

    words_label.config(text="")

    if timer_id:
        window.after_cancel(timer_id)

    seconds = 60
    timer_started = False
    timer_label.config(text=f"Time: {seconds} seconds")
    my_entry.config(state="normal")
    my_entry.delete(1.0, "end")
    load_sample()
    my_entry.focus_set()


def calculate_wpm(original, typed):
    global seconds

    if seconds == 0:
        original_words = original.split()
        typed_words = typed.split()

        common_words_count = sum(1 for o, t in zip(original_words, typed_words) if o == t)

        typed_count = len(typed_words)
        accuracy = (common_words_count / typed_count * 100) if typed_count else 0

        words_label.config(
            text=f"Your speed: {common_words_count} WPM | Accuracy: {accuracy:.0f}%"
        )


window = tk.Tk()
window.title("Typing Speed Test App")
window.geometry("1000x800")
window.config(bg=BG)

first_label = tk.Label(
    window,
    text="Text to type",
    fg=TEXT_COLOR,
    bg=BG,
    font=("Arial", 20, "bold")
)
first_label.pack(pady=(15, 0))

sample_entry = tk.Text(
    window,
    bg=SAMPLE_BG,
    fg=TEXT_COLOR,
    wrap="word",
    height=13,
    width=70,
    font=("Arial", 12),
    relief="flat",
    padx=12,
    pady=10,
    highlightthickness=1,
    highlightbackground=BORDER
)
sample_entry.pack(padx=20, pady=15)
load_sample()

second_label = tk.Label(
    window,
    text="Type the text above as fast as you can",
    fg=TEXT_COLOR,
    bg=BG,
    font=("Arial", 20, "bold")
)
second_label.pack()

restart_button = tk.Button(
    window,
    text="RESTART",
    command=restart_timer,
    bg=ACCENT,
    fg="white",
    activebackground=ACCENT_DARK,
    activeforeground="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=20,
    pady=5,
    cursor="hand2"
)
restart_button.pack(pady=8)

my_entry = tk.Text(
    window,
    bg=TYPING_BG,
    fg=TEXT_COLOR,
    wrap="word",
    height=13,
    width=70,
    font=("Arial", 12),
    relief="flat",
    padx=12,
    pady=10,
    highlightthickness=1,
    highlightbackground=BORDER,
    highlightcolor=ACCENT,
    insertbackground=ACCENT
)
my_entry.pack(padx=20, pady=15)

timer_label = tk.Label(
    window,
    text=f"Time: {seconds} seconds",
    fg=TEXT_COLOR,
    bg=BG,
    font=("Arial", 20)
)
timer_label.pack()

words_label = tk.Label(window, text="", fg=TEXT_COLOR, bg=BG, font=("Arial", 14, "bold"))
words_label.pack(pady=5)

my_entry.bind("<Key>", start_timer)
my_entry.focus_set()

window.mainloop()