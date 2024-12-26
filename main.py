import math
import PySimpleGUI as ui
#when refering to it, you have to do ui.(whatever you wish to do) because we named it ui

#window = ui.Window(title="Calculator", layout=[[]], margins=(250,150)).read()


layout = [
    [ui.Text("Choose an operation")]
    #[ui.Button("+")]
    #[ui.Button("-")]
    #[ui.Button("/")]
    #[ui.Button("*")]
    [ui.Button("Off")]
]

#create the window
window = ui.Window("Demo", layout)

#create an event loop, so if something happens, then something else has to happen
while True:
    event, values = window.read()
    #ends the program if user closes window or presses Off button
    if event == "Off" or event == ui.WINDOW_CLOSED:
        break

window.close()

