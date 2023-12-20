import PySimpleGUI as gui
label1=gui.Text("Enter feet: ")
inputbox1=gui.Input(key="feet")

label2=gui.Text("Enter inches: ")
inputbox2=gui.Input(key="inch")

convertbutton=gui.Button("Convert")
output=gui.Text(key="output")

window=gui.Window("Convertor",
                  layout=[[label1, inputbox1],
                          [label2, inputbox2],
                          [convertbutton, output]])

while True:
    event, values= window.read()
    print (event)
    print(values)
    feet=int(values["feet"])
    inch=int(values["inch"])
    metre=str(feet*0.3048+inch*0.0254)+" m"
    window["output"].update(metre)

window.close()