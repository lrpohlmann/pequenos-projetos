from mainloop import mainloop
from gui.janela_principal import JanelaPrincipal
from mapeamento_evento_acao import mapeamento

if __name__ == '__main__':
    mainloop(JanelaPrincipal('Utilitário Tabela Covid-19'), mapeamento)