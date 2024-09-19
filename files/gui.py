import PySimpleGUI as sg
import sys
print("Python executable:", sys.executable)

import os
print("Current working directory:", os.getcwd())

import time
sys.path.append('/Users/seanyoung/PycharmProjects/pythonProject/')
import functions

# Ensure the todos.txt file exists
if not os.path.exists("/todos.txt"):
    with open("/todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todos')
add_button = sg.Button(size=2, image_source="/Users/seanyoung/PycharmProjects/pythonProject/files/add.png", mouseover_colors="LightBlue2",
                       tooltip="Add", key="Add")
list_box = sg.Listbox(values=functions.get_todos('/todos.txt'), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos('/todos.txt')
            new_todo = values['todos'] + "\n"
            todos.append(new_todo)
            functions.write_todos('/todos.txt', todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvectica", 20))
        case "complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvectica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].updates(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
