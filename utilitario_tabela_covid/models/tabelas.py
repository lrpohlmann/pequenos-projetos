import abc
from calendar import c
from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd
from gui.pysimplegui_keys.nomes_das_keys import *

from models.exceptions import (ColunaNecessariaAusenteError,
                               DataParaFiltragemAusenteError,
                               FormatoDeArquivoNaoSuportadoError)
from models.niveis_de_agregacao import (GeradorDeNiveisDeAgregacao,
                                        GeradorDeNiveisDeAgregacaoHorario,
                                        GeradorDeNiveisDeAgregacaoLinha)
from models.nome_colunas import *


class TabelaHorariaFiltradaPorDataInicioEFim:
    def __init__(self, tabela, data_inicio, data_fim):
        self.tabela = tabela
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self._validar_tabela_inicial()

    def _validar_tabela_inicial(self):
        for coluna in COLUNAS_INICIAIS:
            if not coluna in self.tabela.columns:
                raise ColunaNecessariaAusenteError(coluna)

    def gerar_tabela_horaria_diaria_para_periodo_entre_data_inicio_e_data_fim(self) -> pd.DataFrame:
        tabela_horaria_diaria = pd.DataFrame(
            columns=COLUNAS_TABELA_HORARIA_DIARIA)
        return self._gerar_tabela_vigente_em_cada_dia_e_anexar_na_tabela_horaria_diaria(tabela_horaria_diaria)

    def _gerar_tabela_vigente_em_cada_dia_e_anexar_na_tabela_horaria_diaria(self, tabela_horaria_diaria) -> pd.DataFrame:
        periodo_de_dias = self._gerar_range_de_dias_do_periodo()
        tabelas_a_anexar = []
        for dia in periodo_de_dias:
            tabela_filtrada = self._filtrar_tabela_por_dia_especifico(dia)
            self._retirar_data_inicio_e_fim(tabela_filtrada)
            self._inserir_data_na_tabela(dia, tabela_filtrada)
            self._manter_apenas_horarios_realizados_conforme_tipo_do_dia(
                dia, tabela_filtrada)

            tabelas_a_anexar.append(tabela_filtrada)

        return self._anexar_tabelas_vigentes_na_tabela_horaria_diaria(tabelas_a_anexar, tabela_horaria_diaria)

    def _gerar_range_de_dias_do_periodo(self):
        periodo_de_dias = pd.date_range(self.data_inicio, self.data_fim)
        return periodo_de_dias

    def _filtrar_tabela_por_dia_especifico(self, dia):
        tabela_filtrada = self.tabela[(self.tabela[COLUNA_DATA_INICIO] <= dia) & (
            self.tabela[COLUNA_DATA_FIM] >= dia)].copy()
        return tabela_filtrada

    def _retirar_data_inicio_e_fim(self, tabela):
        tabela.drop(COLUNA_DATA_INICIO, 1, inplace=True)
        tabela.drop(COLUNA_DATA_FIM, 1, inplace=True)

    def _inserir_data_na_tabela(self, data, tabela):
        tabela[COLUNA_DATA] = np.datetime64(data)

    def _manter_apenas_horarios_realizados_conforme_tipo_do_dia(self, dia, tabela):
        def e_domingo(x): return x.weekday() == 6
        def e_sabado(x): return x.weekday() == 5
        def e_dia_util(x): return x.weekday() not in [5, 6]

        if not e_domingo(dia):
            tabela[COLUNA_HORARIO_IDA_DOMINGO] = np.nan
            tabela[COLUNA_HORARIO_VOLTA_DOMINGO] = np.nan
        if not e_sabado(dia):
            tabela[COLUNA_HORARIO_IDA_SABADO] = np.nan
            tabela[COLUNA_HORARIO_VOLTA_SABADO] = np.nan
        if not e_dia_util(dia):
            tabela[COLUNA_HORARIO_IDA_SEMANA] = np.nan
            tabela[COLUNA_HORARIO_VOLTA_SEMANA] = np.nan

    def _anexar_tabelas_vigentes_na_tabela_horaria_diaria(self, lista_de_tabelas, tabela_horaria_diaria):
        for tabela in lista_de_tabelas:
            tabela_horaria_diaria = tabela_horaria_diaria.append(
                tabela, ignore_index=True)

        return tabela_horaria_diaria


class TabelaHorariaDiaria:
    def __init__(self, tabela: TabelaHorariaFiltradaPorDataInicioEFim):
        self.tabela = tabela.gerar_tabela_horaria_diaria_para_periodo_entre_data_inicio_e_data_fim()

    def contar_horarios_por_niveis_de_agregacao(self, gerador_niveis: GeradorDeNiveisDeAgregacaoHorario):
        niveis = gerador_niveis.gerar_niveis_de_agregacao()
        if niveis:
            contagem = self.tabela.groupby(niveis).count()
            return contagem[COLUNAS_HORARIOS].copy()
        elif not niveis:
            contagem = self.tabela[COLUNAS_HORARIOS].aggregate('count')
            return contagem.copy()

    def contar_linhas_por_niveis_de_agregacao(self, gerador_de_niveis: GeradorDeNiveisDeAgregacaoLinha):
        niveis = gerador_de_niveis.gerar_niveis_de_agregacao()
        if niveis:
            contagem = self.tabela.groupby(niveis).nunique()
            return contagem[[COLUNA_CODIGO_LINHA]].copy()
        elif not niveis:
            contagem = self.tabela[[COLUNA_CODIGO_LINHA]].aggregate('nunique')
            return contagem.copy()


class TabelaHorariaAgregada:

    def __init__(self, tabela_horaria_diaria: TabelaHorariaDiaria, niveis_de_agregacao):
        self.tabela = tabela_horaria_diaria.contar_horarios_por_niveis_de_agregacao(
            niveis_de_agregacao)


class TabelaLinhaAgregada:
    def __init__(self, tabela_horaria_diaria: TabelaHorariaDiaria, niveis_de_agregacao):
        self.tabela = tabela_horaria_diaria.contar_linhas_por_niveis_de_agregacao(
            niveis_de_agregacao)


class FiltroTabelaHoraria:

    def filtrar_tabela_por_data_inicio_e_data_fim(self) -> TabelaHorariaFiltradaPorDataInicioEFim:
        pass

    def _validar_tabela(self):
        pass


class FiltroTabelaHorariaExcel(FiltroTabelaHoraria):
    def __init__(self, caminho, data_inicio, data_fim=None):
        self.tabela = pd.read_excel(caminho)
        self.data_inicio = np.datetime64(data_inicio)
        self.data_fim = np.datetime64(data_fim)

        self._validar_tabela()
        if not self.data_inicio:
            raise DataParaFiltragemAusenteError()

    def _validar_tabela(self):
        if COLUNA_DATA_INICIO not in self.tabela.columns:
            raise ColunaNecessariaAusenteError(COLUNA_DATA_INICIO)
        if COLUNA_DATA_FIM not in self.tabela.columns:
            raise ColunaNecessariaAusenteError(COLUNA_DATA_FIM)

    def filtrar_tabela_por_data_inicio_e_data_fim(self) -> TabelaHorariaFiltradaPorDataInicioEFim:
        self._converter_datas_para_datetime64()
        self._preencher_data_fim_vazias_na_tabela_para_filtragem()

        tabela_filtrada_pela_data_inicio = self.tabela[self.tabela[COLUNA_DATA_FIM] >= self.data_inicio].copy(
        )
        if self.data_fim:
            tabela_filtrada_por_ambas_datas = tabela_filtrada_pela_data_inicio[
                tabela_filtrada_pela_data_inicio[COLUNA_DATA_INICIO] <= self.data_fim].copy()

        return TabelaHorariaFiltradaPorDataInicioEFim(tabela_filtrada_por_ambas_datas, self.data_inicio, self.data_fim)

    def _preencher_data_fim_vazias_na_tabela_para_filtragem(self):
        data_tampao = np.datetime64('2099-12-31')
        self.tabela[COLUNA_DATA_FIM] = self.tabela[COLUNA_DATA_FIM].fillna(
            data_tampao)

    def _converter_datas_para_datetime64(self):
        self.tabela[COLUNA_DATA_INICIO] = pd.to_datetime(
            self.tabela[COLUNA_DATA_INICIO], errors='coerce')
        self.tabela[COLUNA_DATA_FIM] = pd.to_datetime(
            self.tabela[COLUNA_DATA_FIM], errors='coerce')


def tabela_horaria_filtrada_por_data_inicio_e_fim_factory(kwargs: Dict) -> TabelaHorariaFiltradaPorDataInicioEFim:
    if Path(kwargs.get(ARQUIVO_INICIAL_INPUT)).suffix == '.xlsx':
        return FiltroTabelaHorariaExcel(kwargs.get(ARQUIVO_INICIAL_INPUT), kwargs.get(DATA_INICIO_INPUT), kwargs.get(DATA_FIM_INPUT)).filtrar_tabela_por_data_inicio_e_data_fim()
    else:
        raise FormatoDeArquivoNaoSuportadoError(
            Path(kwargs.get(ARQUIVO_INICIAL_INPUT)).suffix)
