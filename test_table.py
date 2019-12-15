import sqlite3
import tkinter as tk
import tkinter.ttk as ttk


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


conn = sqlite3.connect('db_kartridji.db')
cursor = conn.cursor()
sql = "select * from users"
cursor.execute(sql)
resultbd = cursor.fetchall()

for row in resultbd:
    id, name, pas = row

    print("\nID: {}  Name: {} PASS: {}".format(id, name, pas))

    print(row)



print(resultbd)



root = tk.Tk()
table = Table(root, headings=('ID', 'User Name', 'Passowrd'), rows=(resultbd))
table.pack(expand=tk.YES, fill=tk.BOTH)
root.mainloop()