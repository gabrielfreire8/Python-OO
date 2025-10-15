from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str___(self):
        return f"{self._nome} | {self.categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'.ljust(25)}')
        for i in cls.restaurantes:
            print(f'{i._nome.ljust(25)} | {i.categoria.ljust(25)} | {str(i.media_avaliacoes).ljust(25)} | {i.ativo} ')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if nota < 0 or nota > 5:
            print(f"⚠️ Nota inválida ({nota})! A nota deve estar entre 0 e 5.")
            return  

        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'sem nota'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)
        return media