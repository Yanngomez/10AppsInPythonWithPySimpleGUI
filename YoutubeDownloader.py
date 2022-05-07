###############################################
# Name: YoutubeDownloader                     #
# Date of Build: 30/04/2022                   #
# Author: Gomez Yann Web3 Developer           #
# Resource Use: Youtuber ClearCode            #
# Link of video: https://youtu.be/QeMaWQZllhg #
###############################################
import PySimpleGUI as sg
from pytube import YouTube

def progress_check(stream, chunk, bytes_remaining):
    progress_amount = 100 - round(bytes_remaining / stream.filesize * 100)
    window['-PROGRESSBAR-'].update(progress_amount)

def on_complete(stream, file_path):
    window['-PROGRESSBAR-'].update(0)

sg.theme('Darkred1')

start_layout = [[sg.Input(key = '-INPUT-'), sg.Button('Sumbit')]]
info_tab = [
    [sg.Text('Title:'), sg.Text('', key = '-TITLE-')],
    [sg.Text('Length:'), sg.Text('', key = '-LENGTH-')],
    [sg.Text('View:'), sg.Text('', key = '-VIEW-')],
    [sg.Text('Author:'), sg.Text('', key = '-AUTHOR-')],
    [
        sg.Text('Description::'),
        sg.Multiline('', key = '-DESCRIPTION-', size = (40,20) , no_scrollbar = True, disabled = True)
    ]
]

info_download = [
    [sg.Frame('Best Quality', [[sg.Button('Download', key = '-BEST-'), sg.Text('', key = '-BESTRES-'), sg.Text('', key = '-BESTSIZE-')]])],
    [sg.Frame('Worst Quality', [[sg.Button('Download', key = '-WORST-'), sg.Text('', key = '-WORSTRES-'), sg.Text('', key = '-WORSTSIZE-')]])],
    [sg.Frame('Audio Quality', [[sg.Button('Download', key = '-AUDIO-'), sg.Text('', key = '-AUDIOSIZE-')]])],
    [sg.VPush()],
    [sg.Progress(100, size = (20,20), expand_x = True, key = '-PROGRESSBAR-')]
]

layout = [[sg.TabGroup([[sg.Tab('info', info_tab), sg.Tab('download', info_download)]])]]

window = sg.Window('Youtube Downloader', start_layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Sumbit':
        video_object = YouTube(values['-INPUT-'], on_progress_callback = progress_check, on_complete_callback = on_complete)
        window.close()

        # Video Info
        window = sg.Window('Youtube Downloader', layout, finalize = True)
        window['-TITLE-'].update(video_object.title)
        window['-LENGTH-'].update(f'{round(video_object.length / 60,2)} minutes')
        window['-VIEW-'].update(video_object.views)
        window['-AUTHOR-'].update(video_object.author)
        window['-DESCRIPTION-'].update(video_object.description)

        # Download
        window['-BESTSIZE-'].update(f'{round(video_object.streams.get_highest_resolution().filesize / 1048576,1)} MB')
        window['-BESTRES-'].update(video_object.streams.get_highest_resolution().resolution)

        window['-WORSTSIZE-'].update(f'{round(video_object.streams.get_lowest_resolution().filesize / 1048576, 1)} MB')
        window['-WORSTRES-'].update(video_object.streams.get_lowest_resolution().resolution)

        window['-BESTRES-'].update(f'{round(video_object.streams.get_audio_only().filesize / 1048576, 1)} MB')

    if event == '-BEST-':
        video_object.streams.get_highest_resolution().download()

    if event == '-WORST-':
        video_object.streams.get_lowest_resolution().download()

    if event == '-AUDIO-':
        video_object.streams.get_audio_only().download()

window.close()