from typing import Any, Callable, Dict, List

from PySimpleGUI import Window

from controller.contagens_controller import (
    produzir_tabela_de_contagem_de_horarios,
    produzir_tabela_de_contagem_de_linhas)
from controller.exception_controller import (
    erro_coluna_necessaria_ausente_controller,
    erro_formato_arquivo_input_controller, erro_input_datas_controller,
    erro_input_de_arquivo_controller)
from gui.pysimplegui_keys.nomes_das_keys import *

mapeamento: Dict[str, List[Callable[[Window, str, Dict], Any]]] = {
    CONTAR_HORARIOS: [
        produzir_tabela_de_contagem_de_horarios
    ],
    CONTAR_LINHA: [
        produzir_tabela_de_contagem_de_linhas
    ],
    ERRO_INPUT_ARQUIVO: [
        erro_input_de_arquivo_controller
    ],
    ERRO_FORMATO_ARQUIVO_INPUT: [
        erro_formato_arquivo_input_controller
    ],
    ERRO_COLUNA_NECESSARIA_AUSENTE: [
        erro_coluna_necessaria_ausente_controller
    ],
    ERRO_INPUT_DATAS: [
        erro_input_datas_controller
    ]
}
