from tkinter import*
import sqlite3


def creat_main():
    root2 = Tk()
    root2.title('Главное окно')
    root2.geometry('600x800')
    but_add = Button(text='Добавить', width=15, height=3)
    but_add.pack()
    #connect db
    conn = sqlite3.connect('db_kartridji.db')


    c =conn.cursor()

    #table
    c.execute("""CREATE TABLE kards(
           kart text,
           type text,
           toner text,
           )""")
    c.commit()
    conn.close()
    root2.mainloop()

creat_main()