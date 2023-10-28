import Functions
import PySimpleGUI as gui

label=gui.Text("Type a todo")
box=gui.InputText(tooltip="Enter todo", key="todo")
add=gui.Button("Add")
edit=gui.Button("Edit")
list_box=gui.Listbox(values=Functions.open_read(), key="todos",
                     enable_events=True, size=[45,10])

window=gui.Window("To-Dos",
                  layout=[[label],[box],[add],
                          [list_box,edit]],
                  font=("Arial",15))

while True:
    event, values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos= Functions.open_read()
            new_todo=values["todo"]+"\n"
            todos.append(new_todo)
            Functions.open_write(todos)
            window["todos"].update(values=todos)
        case gui.WIN_CLOSED:
            break
        case "Edit":
            todo_edit=values["todos"][0]
            new_todo=values["todo"]+"\n"
            todos=Functions.open_read()
            index=todos.index(todo_edit)
            todos[index]=new_todo
            Functions.open_write(todos)
            window["todos"].update(values=todos)
        case "todos":
            todo=values["todos"][0]
            window["todo"].update(value=todo)

window.close()