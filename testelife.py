import datetime
import pandas as pd
#importando o arquivo csv com os dados
dados = pd.read_csv("dados.csv")
#Resposta para a pergunta ---> Qual data ocorreu o maior volume geral de negociações?
volume_Max = dados['volume'].max()
Questão1 = dados.loc[dados['volume']==618237630]
print(Questão1)
print('================================================================')
print('O Maior volume geral de negociações ocorreu na seguinte data ===> 2014-02-24.')
print('===============================================================================')

#Resposta para a pergunta ------> A Partir da resposta da pergunta anterior, quais foram as duas ações mais negociadas nesta data?
nData = dados.loc[dados['date']== '2014-02-24']
quantidade = nData.max()
intervalo = dados.iloc[16905 :17361]
maior1 = intervalo.max()
#maior1 é o primeiro Numero maior desta data ------> 103039579
intervalo1= dados.iloc[17362:17387]
maior2 = intervalo1.max()
#maior2 é o segundo volume maior desta data  --->16034244
print('================================================================================')
print('As duas ações mais negociadas nesta data foram =========> 16034244 e 103039579 ')
print('================================================================================')
#Resposta para a pergunta -->Qual dia da semana o volume de ações é maior?
from datetime import date
ano_mes_dia = [ int(x) for x in '2014-02-24'.split('-') ]
d = datetime.date(year=ano, month=mes, day=dia)
print(d.strftime('%A'))
print('===========================================')
print(' Na Segunda-Feira o volume de açoes é maior.')
print('===========================================')

#Qual dia da semana o volume de ações é menor?
volume_Min = dados['volume'].min()
m = dados.loc[dados['volume']==0]
#print(m)
dia_volume_menor = [ int(x) for x in '2016-01-12'.split('-') ]
dia_menor = datetime.date(year=ano, month=mes, day=dia)
print(d.strftime('%A'))
print('===========================================')
print('Na Terça-Feira o volume de açoes é menor')
print('===========================================')