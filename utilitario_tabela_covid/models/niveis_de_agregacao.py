import abc
from typing import Dict, List

import pandas as pd

from models.nome_colunas import *
from gui.pysimplegui_keys.nomes_das_keys import *


class NivelDeAgregacao:
    
    def __init__(self, nome, ordem):
        self.nome = nome
        self.ordem = ordem
        
    def __eq__(self, other):
        if isinstance(other, NivelDeAgregacao):
            return self.nome == other.nome
        else:
            return False
        
    def __lt__(self, other):
        if isinstance(other, NivelDeAgregacao):
            self.ordem < other.ordem
        else:
            return False
        
    def __gt__(self, other):
        if isinstance(other, NivelDeAgregacao):
            self.ordem > other.ordem
        else:
            return False
        
    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return self.nome


class GeradorDeNiveisDeAgregacao(abc.ABC):
    
    @abc.abstractmethod
    def gerar_niveis_de_agregacao(self) -> List[str]:
        pass
    

class GeradorDeNiveisDeAgregacaoPySimpleGui(GeradorDeNiveisDeAgregacao):
    
    mapeamento_pysimplegui_key_para_nivel = {}
    
    def __init__(self, pysimplegui_keys_value: Dict):
        self.keys_value = pysimplegui_keys_value
        
    def gerar_niveis_de_agregacao(self) -> List[str]:
        chaves = self.keys_value.keys() & self.mapeamento_pysimplegui_key_para_nivel.keys()
        niveis_de_agregacao = [self.mapeamento_pysimplegui_key_para_nivel[k] for k in chaves if self.keys_value.get(k)]
        niveis_de_agregacao.sort(key=lambda x: x.ordem)
        niveis_de_agregacao = [x.nome for x in niveis_de_agregacao]
        return niveis_de_agregacao


class GeradorDeNiveisDeAgregacaoHorario(GeradorDeNiveisDeAgregacaoPySimpleGui):
    
    mapeamento_pysimplegui_key_para_nivel = {
        NIVEL_AGREGACAO_DE_HORARIO_REGIAO: NivelDeAgregacao(COLUNA_REGIAO, 0),
        NIVEL_AGREGACAO_DE_HORARIO_OS: NivelDeAgregacao(COLUNA_OS, 1),
        NIVEL_AGREGACAO_DE_HORARIO_DIA: NivelDeAgregacao(COLUNA_DATA, 2),
        NIVEL_AGREGACAO_DE_HORARIO_MES: NivelDeAgregacao(pd.Grouper(key=COLUNA_DATA, freq="M"), 2),
        NIVEL_AGREGACAO_DE_HORARIO_ANO: NivelDeAgregacao(pd.Grouper(key=COLUNA_DATA, freq="Y"), 2),
        NIVEL_AGREGACAO_DE_HORARIO_EMPRESA: NivelDeAgregacao(COLUNA_CODIGO_EMPRESA, 3),
        NIVEL_AGREGACAO_DE_HORARIO_LINHA: NivelDeAgregacao(COLUNA_CODIGO_LINHA, 4)
    }
    

class GeradorDeNiveisDeAgregacaoLinha(GeradorDeNiveisDeAgregacaoPySimpleGui):
    
    mapeamento_pysimplegui_key_para_nivel = {
        NIVEL_AGREGACAO_DE_LINHA_REGIAO: NivelDeAgregacao(COLUNA_REGIAO, 0),
        NIVEL_AGREGACAO_DE_LINHA_OS: NivelDeAgregacao(COLUNA_OS, 1),
        NIVEL_AGREGACAO_DE_LINHA_DIA: NivelDeAgregacao(COLUNA_DATA, 2),
        NIVEL_AGREGACAO_DE_LINHA_MES: NivelDeAgregacao(pd.Grouper(key=COLUNA_DATA, freq="M"), 2),
        NIVEL_AGREGACAO_DE_LINHA_ANO: NivelDeAgregacao(pd.Grouper(key=COLUNA_DATA, freq="Y"), 2),
        NIVEL_AGREGACAO_DE_LINHA_EMPRESA: NivelDeAgregacao(COLUNA_CODIGO_EMPRESA, 3),
    }


class GeradorDeNiveisDeAgregacaoPySimpleGui(GeradorDeNiveisDeAgregacao):
    
    mapeamento_pysimplegui_key_para_nivel = {}
    
    def __init__(self, pysimplegui_keys_value: Dict):
        self.keys_value = pysimplegui_keys_value
        
    def gerar_niveis_de_agregacao(self) -> List[str]:
        chaves = self.keys_value.keys() & self.mapeamento_pysimplegui_key_para_nivel.keys()
        niveis_de_agregacao = [self.mapeamento_pysimplegui_key_para_nivel[k] for k in chaves if self.keys_value.get(k)]
        niveis_de_agregacao.sort(key=lambda x: x.ordem)
        niveis_de_agregacao = [x.nome for x in niveis_de_agregacao]
        return niveis_de_agregacao


class GeradorDeNiveisDeAgregacaoHorario(GeradorDeNiveisDeAgregacaoPySimpleGui):
    
    mapeamento_pysimplegui_key_para_nivel = {
        NIVEL_AGREGACAO_DE_HORARIO_REGIAO: NivelDeAgregacao(COLUNA_REGIAO, 0),
        NIVEL_AGREGACAO_DE_HORARIO_OS: NivelDeAgregacao(COLUNA_OS, 1),
        NIVEL_AGREGACAO_DE_HORARIO_DIA: NivelDeAgregacao(COLUNA_DATA, 2),
        NIVEL_AGREGACAO_DE_HORARIO_MES: NivelDeAgregacao(pd.Grouper(key=COLUNA_DATA, freq="M"), 2),
        NIVEL_AGREGACAO_DE_HORARIO_ANO: NivelDeAgregacao(pd.Grouper(key=COLUNA_DATA, freq="Y"), 2),
        NIVEL_AGREGACAO_DE_HORARIO_EMPRESA: NivelDeAgregacao(COLUNA_CODIGO_EMPRESA, 3),
        NIVEL_AGREGACAO_DE_HORARIO_LINHA: NivelDeAgregacao(COLUNA_CODIGO_LINHA, 4)
    }
    

class GeradorDeNiveisDeAgregacaoLinha(GeradorDeNiveisDeAgregacaoPySimpleGui):
    
    mapeamento_pysimplegui_key_para_nivel = {
        NIVEL_AGREGACAO_DE_LINHA_REGIAO: NivelDeAgregacao(COLUNA_REGIAO, 0),
        NIVEL_AGREGACAO_DE_LINHA_OS: NivelDeAgregacao(COLUNA_OS, 1),
        NIVEL_AGREGACAO_DE_LINHA_DIA: NivelDeAgregacao(COLUNA_DATA, 2),
        NIVEL_AGREGACAO_DE_LINHA_MES: NivelDeAgregacao(pd.Grouper(key=COLUNA_DATA, freq="M"), 2),
        NIVEL_AGREGACAO_DE_LINHA_ANO: NivelDeAgregacao(pd.Grouper(key=COLUNA_DATA, freq="Y"), 2),
        NIVEL_AGREGACAO_DE_LINHA_EMPRESA: NivelDeAgregacao(COLUNA_CODIGO_EMPRESA, 3),
    }