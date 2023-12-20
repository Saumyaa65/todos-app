import PySimpleGUI as gui
gui.theme("black")

label1=gui.Text("Enter feet: ")
inputbox1=gui.Input(key="feet")

label2=gui.Text("Enter inches: ")
inputbox2=gui.Input(key="inch")

convertbutton=gui.Button("Convert")
exitbutton=gui.Button("Exit")
output=gui.Text(key="output")

window=gui.Window("Convertor",
                  layout=[[label1, inputbox1],
                          [label2, inputbox2],
                          [convertbutton, exitbutton, output]])

while True:
    event, values= window.read()

    match event:
        case "Convert":
            feet=int(values["feet"])
            inch=int(values["inch"])
            metre=str(feet*0.3048+inch*0.0254)+" m"
            window["output"].update(metre)

        case gui.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()