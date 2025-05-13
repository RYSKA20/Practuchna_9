from tkinter import *

def Dobutok(event=None):
    try:
        N = int(edit1.get())
        d = 1
        for i in range(1, N + 1):
            d *= i
        label2['text'] = f"Добуток чисел  1 * 2 * 3 * ... * {N} = {d}"
    except ValueError:
        label2['text'] = "Введіть ціле число!"

root = Tk()
root.geometry("450x150")
root.title("Добуток чисел") 

label1 = Label(root, text="Введіть число:")
label1.place(x=20, y=20)

edit1 = Entry(root)
edit1.place(x=200, y=20, width=240)

# Прив’язка Enter до виклику Dobutok
edit1.bind("<Return>", Dobutok)

label2 = Label(root, text="")
label2.place(x=200, y=50)

root.mainloop()