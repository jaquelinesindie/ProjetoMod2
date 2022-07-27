import pandas as pd
from datetime import datetime

class Pessoa():
    def __init__(self, idade, genero):
        self.idade = idade
        self.genero = genero

    def exibirDados(self):
        return f'Os dados da pessoa foram \nIdade de {self.idade} e gênero segundo as opções {self.genero}'

class Entrevista():
    def __init__(self, perg01, perg02, perg03, perg04):
        self.perg01 = perg01
        self.perg02 = perg02
        self.perg03 = perg03
        self.perg04 = perg04

    def exibirResultado(self):
        return f'As respostas foram {self.perg01}, {self.perg02}, {self.perg03}, {self.perg04}'

""" Variáveis globais
"""
condicao = True # Variavel usada no laço para sair do while quando digitar 00
data_atual = datetime.now().strftime('%Y-%m-%d %H:%M') # Variável que armazena a data e hora atual formatada
respostas = [] # Lista que armazena todas as respostas

while condicao:
    
    escolha_idade = int(input('Digite sua idade: '))

    if escolha_idade == 00:

        print('\nFinalizando as entrevistas. \nObrigado pela atenção!\n')
        condicao = False

    elif escolha_idade != 00:

        escolha_genero = input('Informe seu gênero: \n[1] F \n[2] M \n[3] Outro\n= ')

        objeto_pessoa = Pessoa(escolha_idade, escolha_genero)
        print(objeto_pessoa.exibirDados())
        # print(objeto_pessoa.idade, objeto_pessoa.genero)

        perg01 = input('Você sabia que o mercado de tecnologia no Brasil abre mais de 500 mil vagas por ano? \n[1] Sim\n[2] Não\n[3] Não sei responder\n= ')
        perg02 = input('Você trabalha ou conhece alguém que trabalhe com tecnologia? \n[1] Sim\n[2] Não\n[3] Não sei responder\n= ')
        perg03 = input('Você acredita que o mercado de trabalho tecnológico é diversificado (mulheres, LGBTQIA+, PCD, idade)? \n[1] Sim\n[2] Não\n[3] Não sei responder\n= ')
        perg04 = input('Você acredita que em seis meses um profissional pode estar capacitado para trabalhar nessa área? \n[1] Sim\n[2] Não\n[3] Não sei responder\n= ')

        objeto_pesquisa = Entrevista(perg01, perg02, perg03, perg04)
        print(objeto_pesquisa.exibirResultado())

        respostas.append([escolha_idade, escolha_genero, perg01, perg02, perg03, perg04, data_atual])

    else:
        print('Ocorreu algum problema!')

print('Lista das respostas da pesquisa: ',respostas)



df = pd.DataFrame(respostas)
df.to_csv('teste.csv')
print(df.head())
