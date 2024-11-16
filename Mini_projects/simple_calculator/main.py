# This is my first basic calculator
import tkinter as tk
from help_functions import calculate

# The calculator code
input_calc = ""

def add_to_input_calc(symbol):
    """Function that adds the typed symbol to the displayed output."""
    global input_calc
    # Expand the input of the calculator with the typed symbol
    input_calc += str(symbol)
    # Rewrite the new expanded input onto the screen
    input_text.delete(1.0, "end")
    input_text.insert(1.0, input_calc)

def evaluate_input_calc():
    """The function that will evaluate the input."""
    global input_calc
    # If the user pasted input into the screen directly
    if input_calc == "" or input_calc == "0":
        input_calc = input_text.get("1.0", tk.END)
    try:
        # Compute the result of the calculation with calculate
        input_calc = str(calculate(input_calc))
        input_text.delete(1.0, "end")
        input_text.insert(1.0, input_calc)
    except ZeroDivisionError:
        clear_field()
        input_text.insert(1.0, "Error, cannot divide by zero!")


def clear_field():
    """Function that clears the screen."""
    global input_calc
    input_calc = ""
    input_text.delete(1.0, "end")


# The GUI code
window = tk.Tk("Calculator")
window.geometry("350x400")

# Some constants for personalization
FONT = "Segoe UI"
BUTTON_WIDTH = 5

# The part where the input is displayed
input_text = tk.Text(window, height=2, width=20, font=(FONT, 24))
input_text.grid(columnspan=5)

# The buttons
button_1 = tk.Button(window, text="1", command=lambda: add_to_input_calc(1),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_1.grid(row=2, column=1)

button_2 = tk.Button(window, text="2", command=lambda: add_to_input_calc(2),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_2.grid(row=2, column=2)

button_3 = tk.Button(window, text="3", command=lambda: add_to_input_calc(3),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_3.grid(row=2, column=3)

button_4 = tk.Button(window, text="4", command=lambda: add_to_input_calc(4),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_4.grid(row=3, column=1)

button_5 = tk.Button(window, text="5", command=lambda: add_to_input_calc(5),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_5.grid(row=3, column=2)

button_6 = tk.Button(window, text="6", command=lambda: add_to_input_calc(6),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_6.grid(row=3, column=3)

button_7 = tk.Button(window, text="7", command=lambda: add_to_input_calc(7),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_7.grid(row=4, column=1)

button_8 = tk.Button(window, text="8", command=lambda: add_to_input_calc(8),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_8.grid(row=4, column=2)

button_9 = tk.Button(window, text="9", command=lambda: add_to_input_calc(9),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_9.grid(row=4, column=3)

button_0 = tk.Button(window, text="0", command=lambda: add_to_input_calc(0),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_0.grid(row=5, column=2)

button_add = tk.Button(window, text="+", command=lambda: add_to_input_calc("+"),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_add.grid(row=2, column=4)

button_sub = tk.Button(window, text="-", command=lambda: add_to_input_calc("-"),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_sub.grid(row=3, column=4)

button_mul = tk.Button(window, text="*", command=lambda: add_to_input_calc("*"),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_mul.grid(row=4, column=4)

button_div = tk.Button(window, text="/", command=lambda: add_to_input_calc("/"),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_div.grid(row=5, column=4)

button_open = tk.Button(window, text="(", command=lambda: add_to_input_calc("("),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_open.grid(row=5, column=1)

button_close = tk.Button(window, text=")", command=lambda: add_to_input_calc(")"),
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_close.grid(row=5, column=3)

button_equal = tk.Button(window, text="=", command=evaluate_input_calc,
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_equal.grid(row=6, column=3)

button_clear = tk.Button(window, text="Clear", command=clear_field,
                     width=BUTTON_WIDTH, font=(FONT, 14))
button_clear.grid(row=6, column=2)

window.mainloop()