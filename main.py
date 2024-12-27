import math
import PySimpleGUI as ui
#when refering to it, you have to do ui.(whatever you wish to do) because we named it ui

#window = ui.Window(title="Calculator", layout=[[]], margins=(250,150)).read()
text_Color = "#000000"
normal_Button_Color = "#FFFDD0"
equal_Button_Color = "Dark Orange"
outside_Buttons = {'size':(7,2), 'button_color':("black,dark grey")}

layout = [
    [ui.Text("Simple Calculator")],
    [ui.Text("Answer Temp Placer")],
    [ui.Button("C"),ui.Button("CE"), ui.Button("%"), ui.Button("/")],
    [ui.Button("7"),ui.Button("8"),ui.Button("9"),ui.Button("*")],
    [ui.Button("4"),ui.Button("5"),ui.Button("6"),ui.Button("-")],
    [ui.Button("1"),ui.Button("2"),ui.Button("3"),ui.Button("+")],
    [ui.Button("0", size=(7,2), button_color=("#000000,#FFFDD0")),ui.Button(".", size=(5,2),button_color=("#FFFDD0")),ui.Button("=", size=(10,2),button_color=("Dark Orange"))]
]

#create the window
window = ui.Window("Calculator", layout, margins=(100,150))

#create an event loop, so if something happens, then something else has to happen
while True:
    event, values = window.read()
    #ends the program if user closes window or presses Off button
    if event == "Off" or event == ui.WINDOW_CLOSED:
        break

window.close()

