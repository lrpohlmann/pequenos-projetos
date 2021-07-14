from typing import Dict

from gui.pysimplegui_keys.nomes_das_keys import *
from models.exceptions import (ColunaNecessariaAusenteError,
                               FormatoDeArquivoNaoSuportadoError)
from models.niveis_de_agregacao import (GeradorDeNiveisDeAgregacaoHorario,
                                        GeradorDeNiveisDeAgregacaoLinha)
from models.tabelas import (
    TabelaHorariaAgregada, TabelaHorariaDiaria, TabelaLinhaAgregada,
    tabela_horaria_filtrada_por_data_inicio_e_fim_factory)
from PySimpleGUI import Popup, Window


# TODO: rever duplicação de código nas duas funções
def produzir_tabela_de_contagem_de_horarios(gui: Window, evento: str, valor: Dict):
    # TODO: talvez passar validação dos inputs para uma função decoradora...
    if input_arquivos_sao_invalidos(valor):
        gui.write_event_value(ERRO_INPUT_ARQUIVO, None)
    elif input_datas_sao_invalidos(valor):
        gui.write_event_value(ERRO_INPUT_DATAS, None)
    else:
        try:
            contagem_de_horarios = TabelaHorariaAgregada(
                TabelaHorariaDiaria(
                    tabela_horaria_filtrada_por_data_inicio_e_fim_factory(
                        valor)
                ), GeradorDeNiveisDeAgregacaoHorario(
                    valor
                ))
            contagem_de_horarios.tabela.to_excel(
                valor.get(ARQUIVO_FINAL_INPUT), merge_cells=False)

        except FormatoDeArquivoNaoSuportadoError as e:
            gui.write_event_value(ERRO_FORMATO_ARQUIVO_INPUT, e)

        except ColunaNecessariaAusenteError as e:
            gui.write_event_value(ERRO_COLUNA_NECESSARIA_AUSENTE, e)

        except Exception as e:
            Popup('Erro no processamento.', title='Erro')
            print(e)
        
        finally:
            Popup('Processo Encerrado.')


def produzir_tabela_de_contagem_de_linhas(gui: Window, evento: str, valor: Dict):
    if input_arquivos_sao_invalidos(valor):
        gui.write_event_value(ERRO_INPUT_ARQUIVO, None)
    elif input_datas_sao_invalidos(valor):
        gui.write_event_value(ERRO_INPUT_DATAS, None)
    else:

        try:
            contagem_linhas = TabelaLinhaAgregada(
                TabelaHorariaDiaria(
                    tabela_horaria_filtrada_por_data_inicio_e_fim_factory(
                        valor
                    )
                ), GeradorDeNiveisDeAgregacaoLinha(valor))
            contagem_linhas.tabela.to_excel(
                valor.get(ARQUIVO_FINAL_INPUT), merge_cells=False)

        except FormatoDeArquivoNaoSuportadoError as e:
            gui.write_event_value(ERRO_FORMATO_ARQUIVO_INPUT, e)

        except ColunaNecessariaAusenteError as e:
            gui.write_event_value(ERRO_COLUNA_NECESSARIA_AUSENTE, e)

        except Exception as e:
            Popup('Erro no processamento.', title='Erro')
            print(e)

        finally:
            Popup('Processo Encerrado.')


def input_arquivos_sao_invalidos(valor: Dict):
    if not valor.get(ARQUIVO_INICIAL_INPUT) or not valor.get(ARQUIVO_FINAL_INPUT):
        return True
    else:
        return False


def input_datas_sao_invalidos(valor: Dict):
    if not valor.get(DATA_INICIO_INPUT) or not valor.get(DATA_FIM_INPUT):
        return True
    else:
        return False
