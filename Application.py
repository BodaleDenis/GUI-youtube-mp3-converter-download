from typing import Text
import PySimpleGUI as sg
from src import constexpr as const
from src import Downloader
from src import DownloadList
sg.theme('DarkGrey14')

layout =[[sg.Text('Youtube Link', size=(12, 1)), sg.InputText(key='-YTLINK-')],
          [sg.Radio('Audio', "FORMAT_CHOSSER", default=True, key='-FORMAT-')],
          [sg.Radio('Video', "FORMAT_CHOSSER", default=False)],
          [sg.Button('Download'), sg.Button('Download list')],
          [sg.Button('Add to list'), sg.Button('View list')],
          [sg.Button('Exit')]
        ]

window = sg.Window('YT downloader', layout)
dlist = DownloadList.DownloadList([])
dwnloader = Downloader.Downloader()

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        # Exit the program
        break
    
    if event == 'Download':
        if values['-YTLINK-'] is const.EMPTY_STRING:
            sg.popup_error(const.ERROR_MESSAGE_EMPTY, title='Missing YouTube link')
        elif values['-FORMAT-'] is True:
            dwnloader.download_single_audio(values['-YTLINK-'])
        else:
            dwnloader.download_single_video(values['-YTLINK-'])
    
    if event == 'Download list':
        list_to_download = dlist.get_link_list()
        dwnloader.set_link_list(list_to_download)
        dwnloader.download_all_audio()

    if event == 'Add to list':
        dlist.add_to_list(values['-YTLINK-'])
        print(dlist.link_list)
    
    if event == 'View list':
        sg.popup_ok((dlist.show_list()))