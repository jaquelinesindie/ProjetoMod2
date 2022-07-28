""" Bibliotecas usadas para transformar em CSV e buscar a data e hora da pesquisa
"""
import pandas as pd
from datetime import datetime

""" Menu inicial para saudação e iniciar a Pesquisa
"""
def menu():
    print('='*70)
    print('\n  Olá, seja bem vindo(a) a pesquisa sobre o Mercado Tech no Brasil! \n')
    print('='*70)
    print('Para melhor análise dos dados, lembre-se de utilizar as opções válidas\n')
    
menu()

""" Orientação a objetos para analisar os dados que estão sendo cadastrados de cada pessoa entrevistada
"""
class Pessoa():
    def __init__(self, idade, nome, genero):
        self.idade = idade
        self._nome = nome
        self.genero = genero

    def setNome(self, nomePessoa):
        self._nome = nomePessoa
    
    def getNome(self):
        return self._nome

class Pesquisa(Pessoa): # Recebe como herança a classe Pessoa, pois a Pesquisa depende da existência da Pessoa
    def __init__(self, idade, nome, genero, perg01, perg02, perg03, perg04):
        Pessoa.__init__(self,idade,nome,genero)
        self.perg01 = perg01
        self.perg02 = perg02
        self.perg03 = perg03
        self.perg04 = perg04

    def resgatarDadosPesquisa(self):
        return f'A pessoa que participou da pesquisa se chama {self.getNome()}, possui {self.idade} anos de idade e se identifica com o gênero {sexo[self.genero]}.\nSuas repostas foram {opcao[self.perg01]}, {opcao[self.perg02]}, {opcao[self.perg03]} e {opcao[self.perg04]}\n'


""" Variáveis globais
"""
condicao = True # Variavel usada no laço para sair do while quando digitar 00
dataHora_atual = datetime.now().strftime('%d-%m-%y %H:%M') # Variável que armazena a data e hora atual formatada
respostas = [] # Lista que armazena todas as respostas
sexo = {'1':"Feminino", '2': 'Masculino', '3': 'Outro'} # Dicionário para buscar o valor da variável genero setada como número
opcao = {'1': 'Sim', '2': 'Não', '3': 'Não sei responder'}


""" Laço de repetição que analisa a idade inserida se for diferente de 00 é feita a pesquisa e inserida em uma lista
"""
while condicao:
    print('Se quiser encerrar o programa digite a idade como um valor inteiro menor ou igual a 0.\n')
    escolha_idade = int(input('Digite sua idade: '))

    if escolha_idade <= 00:

        print('\nFinalizando a entrevista. \nObrigado pela participação!\n')
        condicao = False # Variável setada como False faz o laço de repetição finalizar 

    else:

        nome_entrevistado = input('Informe seu nome: ')
        escolha_genero = input('Informe seu gênero: \n[1] Feminino \n[2] Masculino \n[3] Outro\n= ')

        perg01 = input('Você sabia que a área de tecnologia tem mais de 500 mil vagas abertas só no ano 2022? \n[1] Sim\n[2] Não\n[3] Não sei responder\n= ')

        perg02 = input('Você trabalha ou conhece alguém que trabalhe com tecnologia? \n[1] Sim\n[2] Não\n[3] Não sei responder\n= ')

        perg03 = input('Você acredita que o mercado de trabalho tecnológico é diversificado (raça, gênero, orientação sexual, faixa etária, PCD)? \n[1] Sim\n[2] Não\n[3] Não sei responder\n= ')

        perg04 = input('Você acredita que em seis meses um profissional pode estar capacitado para trabalhar nessa área? \n[1] Sim\n[2] Não\n[3] Não sei responder\n= ')
        
        objeto_pesquisa = Pesquisa(escolha_idade, nome_entrevistado, escolha_genero, perg01, perg02, perg03, perg04) # Passa os valores das variáveis correspondentes a classe 
        print(objeto_pesquisa.resgatarDadosPesquisa()) # Retorno dos dados inseridos para efeito de análise de como está sendo inserido e levado a base de dados

        respostas.append([escolha_idade, escolha_genero, perg01, perg02, perg03, perg04, dataHora_atual]) # A lista exclui o nome por ser um dado confidencial apresentado apenas no terminal e insere a data e hora atual

print('Lista das respostas da pesquisa: ', respostas) # Imprime a lista final com os dados da pesquisa

""" Atribuição da lista final da pesquisa ao documento em CSV
"""
df = pd.DataFrame(respostas)
df.to_csv('pesquisatec.csv')
print(df.head())