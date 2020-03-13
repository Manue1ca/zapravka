from tkinter import *
from tkinter import messagebox

def select_item():
    return

def add_item():
    return

def remove_item():
    return

def update_item():
    return
def clear_text():
    return

def populate_list():
    return

# создаем окно
app = Tk()

# картридж
kart_text = StringVar()
part_label = Label(app, text='Картридж', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=kart_text)
part_entry.grid(row=0, column=1)
# тип
type_text = StringVar()
customer_label = Label(app, text='Тип', font=('bold', 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=type_text)
customer_entry.grid(row=0, column=3)
# тонер
toner_text = StringVar()
retailer_label = Label(app, text='Тонер', font=('bold', 14))
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=toner_text)
retailer_entry.grid(row=1, column=1)
# организация
fromthis_text = StringVar()
price_label = Label(app, text='Организация', font=('bold', 14))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=fromthis_text)
price_entry.grid(row=1, column=3)
# Parts List (Listbox)
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# скролл
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# скролл в листбоксе
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# бинд select
parts_list.bind('<<ListboxSelect>>', select_item)

# кнопки
add_btn = Button(app, text='Добавить', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Удалить', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Редактировать', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Очистить', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('Part Manager')
app.geometry('700x350')

# Populate data
populate_list()

# Start program
app.mainloop()