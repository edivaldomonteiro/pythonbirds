class Pessoa:
    def __init__(self, nome=None, idade=39):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Edivaldo')
    print(p.cumprimentar())
    print(id(p))
    print(p.nome, p.idade)

