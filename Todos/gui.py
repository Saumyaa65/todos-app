import Functions
import PySimpleGUI as gui

label=gui.Text("Type a todo")
box=gui.InputText(tooltip="Enter todo")
add=gui.Button("ADD")

window=gui.Window("To-Dos", layout=[[label],[box],[add]])
window.read()
window.close()