import PySimpleGUI as sg
from pytube import YouTube

class TelaDownloader:
    def __init__(self):
        #layout
        layout = [
            [sg.Text("Cole a URL")],
            [sg.Input(key="link")],
            [sg.Checkbox("Download em HD",key="download_hd")],
            [sg.Checkbox("Download somente audio",key="baixar_audio")],
            [sg.Button("Download")]
        ]
        #instanciar a janela
        janela = sg.Window("YouTube Downloader").layout(layout)

        #salvar os dados
        self.button, self.values = janela.Read()

    def Download_Video(self):
        print("Baixando Video...")
        print(self.values['link'])
        url = self.values['link']
        youtube = YouTube(url)
        print('Titulo do video: ', youtube.title)
        
        res_youtube = youtube.streams.get_lowest_resolution()

        if self.values['baixar_audio']:
            res_youtube = youtube.streams.get_audio_only()
            print("Baixando")
        else:
            if self.values['download_hd']:
                res_youtube = youtube.streams.get_highest_resolution()
                print("Baixando em HD")
            res_youtube.download()

tela = TelaDownloader()
tela.Download_Video()