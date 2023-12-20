import Functions
import PySimpleGUI as gui
import time

gui.theme("DarkTeal6")

now = time.strftime("%d %B %Y %A %X")

clock=gui.Text(now, key="clock")
label=gui.Text("Type a todo")
box=gui.InputText(tooltip="Enter todo", key="todo")
add=gui.Button(size=5, image_source="Images/add.png", mouseover_colors="LightBlue2",
               tooltip="Add Todo", key="Add")
edit=gui.Button(size=5, image_source="Images/edit.png", mouseover_colors="LightBlue2",
               tooltip="Edit Todo", key="Edit")
complete=gui.Button(size=5, image_source="Images/complete.png", mouseover_colors="LightBlue2",
               tooltip="Complete Todo", key="Complete")
exit=gui.Button(size=5, image_source="Images/exit.png", mouseover_colors="LightBlue2",
               tooltip="Exit Todos App", key="Exit")
list_box=gui.Listbox(values=Functions.open_read(), key="todos",
                     enable_events=True, size=[45,10])

window=gui.Window("To-Dos",
                  layout=[[clock],
                          [label],[box,add],
                          [list_box,edit,complete],
                          [exit]],
                  font=("Arial",15))

while True:
    event, values=window.read(timeout=999)
    now=time.strftime("%d %B %Y %A %X")
    window["clock"].update(value=now)

    match event:
        case "Add":
            todos= Functions.open_read()
            new_todo=values["todo"]+"\n"
            todos.append(new_todo)
            Functions.open_write(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_edit=values["todos"][0]
                new_todo=values["todo"]+"\n"
                todos=Functions.open_read()
                index=todos.index(todo_edit)
                todos[index]=new_todo
                Functions.open_write(todos)
                window["todos"].update(values=todos)
            except IndexError:
                gui.Popup("Please select an item first!",
                          font=("Arial", 15))
        case "Complete":
            try:
                todo_complete=values["todos"][0]
                todos=Functions.open_read()
                todos.remove(todo_complete)
                Functions.open_write(todos)
                window["todos"].update(todos)
                window["todo"].update("")
            except IndexError:
                gui.Popup("Please select an item first!",
                          font=("Arial", 15))
        case "todos":
            todo=values["todos"][0]
            window["todo"].update(value=todo)
        case "Exit":
            break
        case gui.WIN_CLOSED:
            break

window.close()