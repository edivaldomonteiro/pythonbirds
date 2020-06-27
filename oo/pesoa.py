class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=18):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return f'Método estático de Clase : {55}'

    @classmethod
    def metodo_de_casse(cls):
        return  f'Método de Classe, retorna classe nome: {cls} e o atrbuto de classe olhos:{cls.olhos}'

if __name__ == '__main__':
    jenny = Pessoa(nome='Jenny')
    bre = Pessoa(nome='Bendon')
    edi = Pessoa(jenny, bre, nome='Edivaldo', idade=39)
    print(edi.cumprimentar())
    print(id(edi))
    print(edi.nome, edi.idade)
    print(edi.filhos[0].nome)
    for filhos in edi.filhos:
        print(filhos.nome)
    edi.sobrenome = 'Monteiro'
    del jenny.filhos
    del bre.filhos
    print(edi.__dict__)
    print(jenny.__dict__)
    print(bre.__dict__)
    print(edi.olhos, jenny.olhos, bre.olhos)
    print(Pessoa.olhos)
    print(Pessoa.metodo_estatico(), edi.metodo_estatico())
    print(Pessoa.metodo_de_casse(), edi.metodo_de_casse())
