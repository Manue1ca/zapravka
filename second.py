from tkinter import*
import sqlite3
from tkinter import messagebox as mb
def condb(event):
    conn = sqlite3.connect('db_kartridji.db')
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    resultbd = cursor.fetchall()
    print(resultbd)
    inputbd = [(1, (txt1.get()), (txt2.get()))]
    print(inputbd)
    if resultbd==inputbd:
        label3 = Label(root, text='Верно')
        label3.pack()
        creat_main()
    else:
        label3=Label(root,text='Не верный логин или пароль')
        label3.pack()

def b1_main_event(event):
    data_add = mb.adddata(title = 'Данные', message='Какие действие производились с картриджем?')

def creat_main():
    root.destroy()
    root2 = Tk()
    root2.title('Главное окно')
    root2.geometry('600x800')
    label_for_buttons=Label(root2, width=200, height=5)
    label_for_buttons.config(bg='#938c8c')
    label_for_buttons.pack()
    b1_main = Button(text = 'Добавить', width=15, height=5)
    b1_main.bind('Button-1', b1_main_event)
    b1_main.pack()


root = Tk()
root.title('Выбор пользователя')
root.geometry('400x400')
label1=Label(root, text='Логин')
label1.pack()
txt1=Entry(root, width=7, font='Arial 14')
txt1.pack()
label2=Label(root, text='Пароль')
label2.pack()
txt2=Entry(root,width=7,font='Arial 14')
txt2.pack()
button1=Button(root,text='Представьтесь',width=25,height=3,bg='#f6ff00',fg='red',font='arial 14')
button1.bind('<Button-1>', condb)
button1.pack()

root.mainloop()