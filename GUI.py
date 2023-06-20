import PySimpleGUI as sg

label = sg.Text("Enter the term you want to search: ")
input_box = sg.InputText(tooltip="Enter search term")
search_button = sg.FileSaveAs("Search")

window = sg.Window('Search the term', layout=[[label], [input_box], [search_button]])
window.read()
window.close()
