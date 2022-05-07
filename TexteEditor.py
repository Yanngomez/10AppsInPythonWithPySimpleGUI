###############################################
# Name: TextEditor                            #
# Date of Build: 27/04/2022                   #
# Author: Gomez Yann Web3 Developer           #
# Resource Use: Youtuber ClearCode            #
# Link of video: https://youtu.be/QeMaWQZllhg #
###############################################
import PySimpleGUI as sg
from pathlib import Path
smileys = [
    'happy', [':)', '*D', ':D', '<3'],
    'sad', [':(', 'T_T'],
    'other', [':3']
]

smiley_events = smileys[1] + smileys[3] + smileys[5]

menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tool', ['Word Count']],
    ['Add', smileys]
]

sg.theme('GrayGrayGray')
layout = [
    [
        [sg.Menu(menu_layout)],
        [sg.Text('Untitled', key = '-DOCNAME-')],
        [sg.Multiline(no_scrollbar = True, size = (40, 30), key = '-TEXTBOX-')]
    ]
]

window = sg.Window('Text Editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Open':
        file_path = sg.popup_get_file('open', no_window = True)
        if file_path:
            file = Path(file_path)
            window['-TEXTBOX-'].update(file.read_text())
            window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event == 'Save':
        file_path = sg.popup_get_file('Save as', no_window = True, save_as = True) + '.txt'
        file = Path(file_path)
        file.write_text(values['-TEXTBOX-'])
        window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event == 'Exit':
        window.close()


    if event == 'Word Count':
        full_text = values['-TEXTBOX-']
        clean_text = full_text.replace('\n', ' ').split(' ')
        char_count = len(clean_text)
        word_count = len(''.join(clean_text))
        sg.popup(f' Words: {word_count}\n Characters: {char_count}')

    if event in smiley_events:
        current_text = values['-TEXTBOX-']
        new_text = current_text + ' ' + event
        window['-TEXTBOX-'].update(new_text)

window.close()