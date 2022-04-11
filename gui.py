from glob import glob
import tkinter as tk
from tkinter import font 

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    


def evaluate_calculation():
    global calculation
    print(calculation)
    try:
        result = str(eval(calculation))
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
        
    except:
        clear_field()
        text_result.insert(1.0, "Error")


    pass


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    text_result.insert(1.0, "")
    pass

root = tk.Tk()
root.geometry("500x400")


text_result = tk.Text(root, height=2, width=22, font=("Arial", 24))
text_result.grid(columnspan=10)

btn_1 = tk.Button(root, text="1", command = lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=3, column=1)
btn_2 = tk.Button(root, text="2", command = lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=3, column=2)
btn_3 = tk.Button(root, text="3", command = lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=3, column=3)
btn_4 = tk.Button(root, text="4", command = lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=4, column=1)
btn_5 = tk.Button(root, text="5", command = lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=4, column=2)
btn_6 = tk.Button(root, text="6", command = lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=4, column=3)
btn_7 = tk.Button(root, text="7", command = lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=5, column=1)
btn_8 = tk.Button(root, text="8", command = lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=5, column=2)
btn_9 = tk.Button(root, text="9", command = lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=5, column=3)
btn_0 = tk.Button(root, text="0", command = lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=6, column=1)

btn_dot = tk.Button(root, text=".", command = lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_dot.grid(row=6, column=2)
btn_equal = tk.Button(root, text="=", command = evaluate_calculation, width=5, font=("Arial", 14), bg="#0098ED")
btn_equal.grid(row=6, column=3)

btn_left_parenthesis = tk.Button(root, text="(", command = lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_left_parenthesis.grid(row=2, column=1)

btn_right_parenthesis = tk.Button(root, text=")", command = lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_right_parenthesis.grid(row=2, column=2)

btn_clear = tk.Button(root, text="C", command = clear_field, width=6, font=("Arial", 14), bg='#CB0535')
btn_clear.grid(row=2, column=5)


btn_factorial = tk.Button(root, text="x!", command = lambda: add_to_calculation("!"), width=6, font=("Arial", 14))
btn_factorial.grid(row=3, column=5)

btn_root = tk.Button(root, text="√", command = lambda: add_to_calculation("√"), width=5, font=("Arial", 14))
btn_root.grid(row=2, column=3)

btn_power = tk.Button(root, text="x\u02b8", command = lambda: add_to_calculation("^"), width=5, font=("Arial", 14))
btn_power.grid(row=2, column=4)

# btn_advanced_mod = tk.Button(root, text="Advanced", command = lambda: add_to_calculation(1), width=5, font=("Arial", 14))
# btn_advanced_mod.grid(rowspan = 2, row = 3, column=5)

btn_devide = tk.Button(root, text="÷", command = lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_devide.grid(row=3, column=4)

btn_multiplie = tk.Button(root, text="*", command = lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_multiplie.grid(row=4, column=4)

btn_plus = tk.Button(root, text="+", command = lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=5, column=4)

btn_minus = tk.Button(root, text="-", command = lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=6, column=4) 




root.mainloop()