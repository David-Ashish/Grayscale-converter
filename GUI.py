import PySimpleGUI as sg
from Practice import foo

label = sg.Text("Enter the password ")
input_box = sg.InputText(key='password')
check_button = sg.Button("Check")

window = sg.Window('Enter the password', layout=[[label], [input_box], [check_button]])
window.read()
window.close()
