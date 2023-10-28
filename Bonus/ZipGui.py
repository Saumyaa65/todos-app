import PySimpleGUI as gui
from ZIP import make_archive


label1=gui.Text("Select files to compress")
input=gui.Input()
ch1=gui.FileBrowse("Choose", key="files")

label2=gui.Text("Select destination folder")
input2=gui.Input()
ch2=gui.FolderBrowse("Choose", key="folder")

com=gui.Button("Compress")
output= gui.Text(key="output")

window=gui.Window("Compressor",
                  layout=[[label1],[input,ch1],
                          [label2],[input2,ch2],
                          [com, output]])
while(True):
    event, values = window.read()
    print(event,values)
    filepaths= values["files"].split(";")
    folder=values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed")

window.close()
