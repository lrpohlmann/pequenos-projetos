from typing import Dict

from PySimpleGUI import Popup, Window


def erro_input_de_arquivo_controller(gui: Window, evento: str, valor: Dict):
    Popup('Arquivo inicial e/ou final não específicado.', title='Atenção')


def erro_input_datas_controller(gui: Window, evento: str, valor: Dict):
    Popup('Datas não foram escolhidas.', title='Atenção')


def erro_formato_arquivo_input_controller(gui: Window, evento: str, valor: Dict):
    erro = valor.get(evento)
    Popup(str(erro), title='Erro')


def erro_coluna_necessaria_ausente_controller(gui: Window, evento: str, valor: Dict):
    erro = valor.get(evento)
    Popup(str(erro), title='Erro')
