
from tkinter import*
task_list = []


def add_task():
    current = input_task.get()
    if current != "":
        input_task.delete(0, END)
        task_list.append(current)
        lb.delete(0, END)
        for item in task_list:
            lb.insert(END, item)
    else:
        return -1


def delete_task():
    lb.delete(ANCHOR)

    # header
root = Tk()
root.title("Todo List App")
root.geometry("500x300+250+250")
root.resizable(0, True)


# new widget
frame = Frame(root)
header = Label(root, text="Todo List App", font=(
    "Comic Sans MS", 20, "bold"), bg="#F6E7D8")
lb = Listbox(
    width=5,
    height=5,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    bg="#F68989",
    justify=CENTER,
    activestyle="none",
    highlightthickness=0,
    selectbackground="#C65D7B")
label_input_name = Label(root, text="Task's name:", bg="#F6E7D8")
input_task = Entry(root, borderwidth=0, width=20)
button_add = Button(root, text="Add Task", borderwidth=0,
                    bg="#77dd77", padx=6.5, command=add_task)
button_delete = Button(root, text="Delete Task",
                       borderwidth=0, bg="#F68989", command=delete_task)
scrollbar = Scrollbar(root)
# config
lb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lb.yview)
root.config(bg="#F6E7D8")
# packing
header.pack()
lb.pack(fill=BOTH)
button_add.pack(side=LEFT)
button_add.place(x=175, y=250)
label_input_name.pack()
input_task.pack(pady=5)
button_delete.pack(side=LEFT)
button_delete.place(x=255, y=250)
scrollbar.pack(side=RIGHT, fill=BOTH)
root.mainloop()