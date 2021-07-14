from PySimpleGUI import (
    Frame, Input, FileSaveAs
)

from gui.pysimplegui_keys.nomes_das_keys import *


class FrameArquivoSaida(Frame):

    def __init__(self):
        layout = [
            [Input(k=ARQUIVO_FINAL_INPUT), FileSaveAs('...', k='BTN_SAIDA', file_types=(('Excel', '*.xlsx'),))]
        ]

        super().__init__('Arquivo Saída', layout=layout)