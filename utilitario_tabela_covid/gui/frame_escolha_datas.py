from PySimpleGUI import (
    Frame, CalendarButton
)
from PySimpleGUI.PySimpleGUI import Input

from gui.pysimplegui_keys.nomes_das_keys import *


class EscolhaData(Frame):
    
    def __init__(self, formato_datas="%Y-%m-%d"):
        data_inicio = CalendarButton('', format=formato_datas)
        data_fim = CalendarButton('', format=formato_datas)

        layout = [
            [Input('', k=DATA_INICIO_INPUT), data_inicio],
            [Input('', k=DATA_FIM_INPUT), data_fim]
        ]

        super().__init__('Escolha Período', layout=layout)