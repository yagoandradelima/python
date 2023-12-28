# Criando a classe pai
class Cliente:
    # Criando a função construtora
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    
    # Criando um método de assinatura
    def assinar(self, assinatura):
        self.lista_assinatura = ['básico', 'padrão', 'premium']
        if assinatura in self.lista_assinatura:
            self.assinatura = assinatura
            return assinatura
        else:
            return 'Assinatura não é válida'

# Classe filha
class ClientePremium(Cliente):
    # função construtora da classe filha
    def __init__(self, nome, idade, email, filmes):
        # Puxando atributos da classe pai
        super().__init__(nome, idade, email)
        # Atributo da classe filha
        self.filmes = filmes
    
# Criando objeto instanciando a classe filha
yago_andrade = ClientePremium('Yago', 25, 'yago@gmail.com', 'FilmesPremium')

# Verificando se o atributo possui valor
print(yago_andrade.filmes)

# Acessando um método da Classe Pai tendo instanciado a Classe Filha
print(yago_andrade.assinar('premium'))