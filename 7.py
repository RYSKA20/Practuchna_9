from tkinter import *

def Factorial(event=None):
    try:
        N = int(edit1.get())
        f = 1
        for i in range(1, N + 1):
            f *= i
        label2['text'] = f"Факторіал числа {N}! = {f}"
    except ValueError:
        label2['text'] = "Введіть ціле число!"

root = Tk()
root.geometry("420x150")
root.title("Факторіал") 

label1 = Label(root, text="Введіть число N  : ")
label1.place(x=20, y=20)

edit1 = Entry(root)
edit1.place(x=200, y=20, width=200)

# Прив’язка Enter до виклику Factorial
edit1.bind("<Return>", Factorial)

label2 = Label(root, text="")
label2.place(x=200, y=50)

root.mainloop()