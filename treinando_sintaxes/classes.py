class ControleRemoto:
    def __init__(self, cor, largura, comprimento, profundidade):
        self.cor = 'preto'
        self.largura = '2cm'
        self.comprimento = '15cm'
        self.profundidade = '2cm'

    def passar_canal(self, botao):
        if botao == '+':
            print('Aumentar o canal')
        elif botao == '-':
            print('Diminuir o canal')
        

controle_tv = ControleRemoto('branco', '3cm', '10cm', '2cm')
controle_lampada = ControleRemoto('Cinza', '4cm', '7cm', '3cm')

print(f'A cor do controle da TV é {controle_tv.cor}')
print(f'A cor do controle da lâmpada é {controle_lampada.cor}')
controle_tv.passar_canal('+')