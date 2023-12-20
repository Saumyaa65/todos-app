import PySimpleGUI as gui
from ZipExtractor import extract_archive

gui.theme("DarkBlue2")

label1=gui.Text("Select archive")
input1=gui.Input()
button1=gui.FileBrowse("Choose", key= "archive")

label2=gui.Text("Select Destination")
input2=gui.Input()
button2=gui.FolderBrowse("Choose", key= "folder")

button3=gui.Button("Extract")
label3=gui.Text(key= "output", text_color="green")

window=gui.Window("Archive Extractor",
                  [[label1, input1, button1],
                        [label2, input2, button2],
                         [button3, label3]])

while True:
    event, value= window.read()
    print (event, value)
    path=value["archive"]
    des=value["folder"]
    extract_archive(path, des)
    window["output"].update(value="Extraction Completed")

window.close()