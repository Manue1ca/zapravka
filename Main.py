from tkinter import*
import sqlite3

def creat_main():
    root2 = Tk()
    root2.title('Главное окно')
    root2.geometry('600x800')
    but_add = Button(text='Добавить', width=15, height=3)
    but_add.bind('<Button-1>', ev_add)
    but_add.bind('<Return>', ev_add)
    but_add.pack()

    root2.mainloop()
#событие по нажатию кнопки добаить в главном меню
def ev_add(event):
    # действие subm_btn command=submit
    def submit(event):
        conn = sqlite3.connect('db_kartridji.db')
        c = conn.cursor()
        c.execute("INSERT INTO kart VALUES (:kart, :type, :toner)",
                  {
                      'kart': kart.get(),
                      'type': Type.get(),
                      'toner': Toner.get()
                  })
        conn.commit()
        conn.close()
        kart.delete(0,END)
        Type.delete(0, END)
        Toner.delete(0, END)
    root3 = Tk()
    root3.title('Окно добавления')
    root3.geometry('400x200+400+400')
    root3.resizable(False,False)
    root3.grab_set()
    root3.focus_set()
    #создание полей ввода
    kart = Entry(root3, width=30)
    kart.grid(row=1, column=1, padx=20)
    Type = Entry(root3, width=30)
    Type.grid(row=3, column=1, padx=20)
    Toner = Entry(root3, width=30)
    Toner.grid(row=5, column=1, padx=20)
    # создание лейблов
    kart_label = Label(root3, text='Картридж')
    kart_label.grid(row=0, column=1)
    Type_label = Label(root3, text='Тип')
    Type_label.grid(row=2, column=1)
    Toner_label = Label(root3, text='Тонер')
    Toner_label.grid(row=4, column=1)
    subm_btn = Button(root3, text='Добавить',)
    subm_btn.bind('<Button-1>', submit)
    subm_btn.grid(row=6, column=0, columnspan=2, pady=20, padx=20, ipadx=10)

creat_main()

