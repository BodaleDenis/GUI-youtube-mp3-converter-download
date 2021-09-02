from typing import Text
import PySimpleGUI as sg
from src import constexpr as const
from src import Downloader
sg.theme('DarkGrey14')

layout =[[sg.Text('Youtube Link', size=(12, 1)), sg.InputText(key='-YTLINK-')],
          [sg.Radio('Audio', "FORMAT_CHOSSER", default=True, key='-FORMAT-')],
          [sg.Radio('Video', "FORMAT_CHOSSER", default=False)],
          [sg.Button('Download')],
          [sg.Button('Exit')]
        ]

window = sg.Window('YT downloader and converter', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        # Exit the program
        break
    if event == 'Download':
        if values['-YTLINK-'] is None:
            print('NOT OK')
        elif values['-FORMAT-'] is True:
            Downloader.download(values['-YTLINK-'], const.AUDIO_FORMAT)
        else:
            Downloader.download(values['-YTLINK-'], const.VIDEO_FORMAT)

