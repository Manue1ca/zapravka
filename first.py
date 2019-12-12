from tkinter import*
import sqlite3

conn = sqlite3.connect('db_kartridji.db')
cursor = conn.cursor()

root = Tk()
root.title('Выбор пользователя')
root.geometry('400x400')
label1=Label(root, text='Логин')
label1.pack()
text1=Text(root,height=1,width=7,font='Arial 14',wrap=WORD)
text1.pack()
label2=Label(root, text='Пароль')
label2.pack()
text2=Text(root,height=1,width=7,font='Arial 14',wrap=WORD)
text2.pack()
button1=Button(root,text='Представьтесь',width=25,height=3,bg='#f6ff00',fg='red',font='arial 14')
button1.pack()

root.mainloop()