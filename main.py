from tkinter import *




# GUI
win = Tk()
win.title("Добро пожаловать в приложение PythonRu")
win.geometry('400x250')
txt = Label(text='добро пожаловать, определяйся что ты хочешь сделать')
txt.grid(column=0, row= 0)
btn = Button(win, text = 'Добавить нового пользователя')
btn.grid(column=0, row=1)
btn= Button(win, text = 'Найти существующего пользователя')
btn.grid(column=0, row=2)
btn = (win)

win.mainloop()
