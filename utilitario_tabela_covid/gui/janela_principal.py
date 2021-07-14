from typing import Text
from PySimpleGUI import (
    Window, WIN_CLOSED, change_look_and_feel
)
from PySimpleGUI.PySimpleGUI import Column

from gui.frame_escolha_datas import EscolhaData
from gui.frame_niveis_de_agregacao import EscolhaContagens
from gui.frame_input_arquivo_entrada import FrameArquivoEntrada
from gui.frame_input_arquivo_saida import FrameArquivoSaida

change_look_and_feel('SystemDefault')


class JanelaPrincipal(Window):

    def __init__(self, title):
        layout = [
            [Column(layout=[
                [FrameArquivoEntrada()],
                [EscolhaData()],
                [FrameArquivoSaida()],  
            ]),
            Column(layout=[
                [EscolhaContagens()],
            ])]
        ]
        super().__init__(title=title, layout=layout)


if __name__ == '__main__':
    janela = JanelaPrincipal('1')
    while True:
        evento, valor = janela.read()
        print(evento, valor)
        if evento in (WIN_CLOSED, None):
            janela.close()
            break