class FormatoDeArquivoNaoSuportadoError(Exception):

    def __init__(self, formato_arquivo: str) -> None:
        mensagem = f'O seguinte formato de arquivo não é suportado: {formato_arquivo}'
        super().__init__(mensagem)


class ColunaNecessariaAusenteError(Exception):

    def __init__(self, coluna_ausente: str) -> None:
        self.coluna_ausente = coluna_ausente
        mensagem = f'Coluna ausente: {self.coluna_ausente}'
        super().__init__(mensagem)


class DataParaFiltragemAusenteError(Exception):

    def __init__(self) -> None:
        super().__init__('Data ausente')
