# Classe pai para cliente simples
class Cliente:
    # Função construtora para clientes
    def __init__(self, nome, cpf, numero, conta):
        self.nome = nome
        self._cpf = cpf
        self.numero = numero
        self.__conta = conta

    # Método Especial get para atributo privado
    def getConta(self):
        return self.__conta
    
    # Método Especial set para atributo privado
    def setConta(self, novo_conta):
        if len(novo_conta) > 6:
            self.__conta = novo_conta
        else:
            return 'Conta Inválida'
    
    # Método Especial get para atributo protegido
    def getCPF (self):
        return self._cpf
    
    # Método Especial set para atributo protegido
    def setCPF (self, novo_cpf):
        if len(novo_cpf) > 11:
            self._cpf = novo_cpf
        else:
            return 'CPF Inválido'

# Classe Filha
class Correntista(Cliente):
    # Função construtora da Classe Filha
    def __init__(self, nome, cpf, numero, agencia, conta):
        # Herança da função pai
        super().__init__(nome, cpf, numero, conta)
        # Atributo Classe Filha
        self._agencia = agencia

    # Método Especial get para atributo protegido
    def getAgencia(self):
        return self._agencia

    # Método Especial set para atributo protegido
    def setAgencia(self, novo_Agencia):
        if len(novo_Agencia) >= 3:
            self._agencia = novo_Agencia
        else:
            return 'Agencia inválida'

# Criando objeto a partir da Classe Filha
jk_silva = Correntista('JK', '12345678900', '9199999999', '1234567', '12345')

# Testando um print do atributo protegido CPF
print(jk_silva._cpf)

# Testando um print do método especial para acessar o atributo privado __conta
print(jk_silva.getConta())

# Utilizando o método set para atualizar o valor
print(jk_silva.setConta('789456455'))

# Printando o novo valora pra conta
print(jk_silva.getConta())


"""
 Esse print retorna um erro, pois __conta não está dentro da Classe Filha

 Por ser uma tributo PRIVADO só a Classe Cliente (e objetos criados por ela) 
 tem acesso a esse atributo
"""
print(jk_silva.__conta)