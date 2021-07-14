from typing import Dict

from mapeamento_evento_acao import mapeamento

from PySimpleGUI import (
    Window, 
    WIN_CLOSED,
)


def mainloop(gui: Window, mapeamento: Dict):
    while True:
        evento, valor = gui.read()
        if evento in (None, WIN_CLOSED):
            gui.close()
            break
        elif mapeamento.get(evento):
            for acao in mapeamento.get(evento):
                acao(gui, evento, valor)
            