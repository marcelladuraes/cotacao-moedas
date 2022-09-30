import requests
import json
import sqlite3
import datetime

requisicao = requests.get('https://api.hgbrasil.com/finance?key=2ebfe9dd')
valor = json.loads(requisicao.text)
'''print(valor) '''
dolar = valor['results']['currencies']['USD']['buy']
euro = valor['results']['currencies']['EUR']['buy']
real = float(input('Informe o valor desejado em reais: '))
dolarConvertido = real/dolar
euroConvertido = real/euro
data_hora = datetime.datetime.now()
print(f'Valor em dolar: {dolarConvertido}')
print(f'Valor em euro: {euroConvertido}')
print(f'Data e hora: {data_hora}')

conexao = sqlite3.connect('cotacoes.db')
cursor = conexao.cursor()
# cursor.execute("CREATE TABLE cotacao (dolar real, euro real, data_hora text)") A LINHA FOI COMENTADA APÓS A CRIAÇÃO DA TABELA
cursor.execute("INSERT INTO cotacao (dolar, euro, data_hora) VALUES (?,?,?);", (dolar,euro,data_hora))
conexao.commit()
cursor.execute("SELECT * FROM Cotacao")
print(cursor.fetchall())