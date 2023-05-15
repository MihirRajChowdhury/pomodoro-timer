from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
REPS = 0
time = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global REPS
    timer.config(text="Timer",fg=GREEN)
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text=f"00:00")
    REPS = 0
    tick.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 1)
        timer.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 1)
        timer.config(text="Break", fg=PINK)

    else:
        count_down(WORK_MIN * 1)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global time
    minutes = math.floor(count / 60)
    seconds = (count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    if count > -1:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        marks = ""
        for _ in range(math.floor(REPS / 2)):
            marks += "🗸"
        tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro App")
# window.minsize(height=200, width=300)
window.config(padx=100, pady=50, bg=YELLOW)

# Timer label in the screen
timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
timer.grid(column=1, row=0)

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Start and Reset button code

start = Button(text="Start", highlightthickness=0, width=5, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", width=5, highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

# Tick label of at the last
tick = Label(font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=3)

window.mainloop()
