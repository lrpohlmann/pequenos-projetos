from PySimpleGUI import (
    Frame, Input, FileBrowse
)

from gui.pysimplegui_keys.nomes_das_keys import *


class FrameArquivoEntrada(Frame):

    def __init__(self):

        layout = [
            [Input(k=ARQUIVO_INICIAL_INPUT), FileBrowse('...', file_types=(('Excel', '*.xlsx'),))]
        ]

        super().__init__("Arquivo Entrada", layout=layout)