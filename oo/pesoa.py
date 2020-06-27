class Pessoa:
    def __init__(self, *filhos, nome=None, idade=18):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


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

