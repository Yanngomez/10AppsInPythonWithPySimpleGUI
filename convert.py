###############################################
# Name: Convert                               #
# Date of Build: 25/04/2022                   #
# Author: Gomez Yann Web3 Developer           #
# Resource Use: Youtuber ClearCode            #
# Link of video: https://youtu.be/QeMaWQZllhg #
###############################################
import PySimpleGUI as sg

layout = [
    [
        sg.Input(key = '-INPUT-'),
        sg.Spin(['Km to mile','Kg to pound','Sec to min'], key = '-UNITS-'),
        sg.Button('Convert', key = '-CONVERT-')
    ],
    [sg.Text('OUTPUT', key = '-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'Km to mile':
                    output = round(float(input_value) * 0.6214,2)
                    output_string = f' {input_value} km are {output} mile.'
                case 'Kg to pound':
                    output = round(float(input_value) * 2.20462,2)
                    output_string = f' {input_value} kg are {output} pounds.'
                case 'Sec to min':
                    output = round(float(input_value) / 60,2)
                    output_string = f' {input_value} seconds are {output} minutes.'

            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please Djobie enter number')

window.close()