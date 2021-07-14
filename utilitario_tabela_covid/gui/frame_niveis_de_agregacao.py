from PySimpleGUI import (
    Frame, TabGroup, Tab, Checkbox, Button
)

from gui.pysimplegui_keys.nomes_das_keys import *


class EscolhaContagens(Frame):

    def __init__(self):

        layout = [
            [_TabGroupContagens()]
        ]

        super().__init__('Níveis de Agregação para contagem', layout=layout)        

class _TabGroupContagens(TabGroup):

    def __init__(self):

        layout = [
            [_TabContagemHorarios(), _TabContagemLinhas()]
        ]

        super().__init__(layout=layout)

class _TabContagemHorarios(Tab):

    def __init__(self):

        layout = [
            [Checkbox('Por OS', k=NIVEL_AGREGACAO_DE_HORARIO_OS)],
            [Checkbox('Por Ano', k=NIVEL_AGREGACAO_DE_HORARIO_ANO)],
            [Checkbox('Por Região', k=NIVEL_AGREGACAO_DE_HORARIO_REGIAO)],
            [Checkbox('Por Mês', k=NIVEL_AGREGACAO_DE_HORARIO_MES)],
            [Checkbox('Por Dia', k=NIVEL_AGREGACAO_DE_HORARIO_DIA)],
            [Checkbox('Por Empresa', k=NIVEL_AGREGACAO_DE_HORARIO_EMPRESA)],
            [Checkbox('Por Linha', k=NIVEL_AGREGACAO_DE_HORARIO_LINHA)],
            [Button('Contar Horários', enable_events=True, k=CONTAR_HORARIOS)]
        ]

        super().__init__('Contagem Horários', layout=layout)


class _TabContagemLinhas(Tab):

    def __init__(self):

        layout = [
            [Checkbox('Por OS', k=NIVEL_AGREGACAO_DE_LINHA_OS)],
            [Checkbox('Por Ano', k=NIVEL_AGREGACAO_DE_LINHA_ANO)],
            [Checkbox('Por Região', k=NIVEL_AGREGACAO_DE_LINHA_REGIAO)],
            [Checkbox('Por Mês', k=NIVEL_AGREGACAO_DE_LINHA_MES)],
            [Checkbox('Por Dia', k=NIVEL_AGREGACAO_DE_LINHA_DIA)],
            [Checkbox('Por Empresa', k=NIVEL_AGREGACAO_DE_LINHA_EMPRESA)],
            [Button('Contar Linhas', enable_events=True, k=CONTAR_LINHA)]
        ]

        super().__init__('Contagem Linhas', layout=layout)