from tkinter import *
import math

root = Tk()
root.title("MATHEOS by hazal-hk")

expression = StringVar()
result = StringVar()

Label(root, font=('Times', 25, 'bold'), textvariable=expression, height=2).grid(columnspan=4, ipadx=120)
Label(root, font=('Times', 25, 'bold'), textvariable=result, height=2).grid(columnspan=4, ipadx=120)

def onButtonClick(entry):
    if entry == "AC":
        expression.set("")
        result.set("")
    elif entry == "=":
        try:
            res = eval(expression.get())
            result.set(res)
            expression.set(str(res))  
        except:
            result.set("Error")
            expression.set("")
    elif entry == "sqrt":
        try:
            res = math.sqrt(float(expression.get()))
            result.set(res)
            expression.set(str(res))
        except:
            result.set("Error")
            expression.set("")
    else:
        expression.set(expression.get() + str(entry))

buttons = [
    ("AC", "sqrt", "%", "/"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("0", ".", "=", None)
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text:
            Button(root, text=text, font=('Times', 15, 'bold'), padx=16, pady=16, height=2, width=9,
                   command=lambda t=text: onButtonClick(t)).grid(row=i + 3, column=j, sticky=E)

root.mainloop()
