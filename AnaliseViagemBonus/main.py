import pandas as pd
#from twilio.rest import Client

# Your Account SID from twilio.com/console
#account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
#auth_token  = "your_auth_token"
#client = Client(account_sid, auth_token)

# exercicio para praticar python
# exemplo na video aula retirado do youtube
# Passo a passo para resuloção do exercico
# Abrir os 6 arquivos em Excel
# Para cada arquivo:
# Verificar se algum valor da coluno da Vendas daqueles arquivos é maior que 55.000
# Se for maior que 55.000 -> envia sms com o nome, o mes e as vendas do vendedor
# Nesse exemplo não irei fazer a parte que envia o SMS, pois precisa criar uma conta no twilio e o periodo teste é de 30 dias,
# pretendo deixar esse periodo de teste para quando tiver mais pojetos.
# Bibliotecas: Pandas, Openpyxl, Twilio
# instalações necessárias: pandas (para ler os arquivos excel), openpyxl (necessário para leitura dos arquivos excel),
# twilio (envio de sms - como mencionei nao irei instalar)
# Abir os aquivos

lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 30000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 30000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 30000,'Vendas'].values[0]
        print(f' No mes de {mes} o vendedor: {vendedor} que bateu a meta com o valor de R$ {vendas}')
        # para envio de sms com as informações: esse comentário SUBSTITUI o print da linha acima
        #message = client.messages.create(
            #to="Para quem ira enviar ex: +15558675309", 
            #from_="quando cria uma conta no twilio ganha um numero para teste ex:+15017250604",
            #body=f' No mes de {mes} o vendedor: {vendedor} que bateu a meta com o valor de R$ {vendas}')

        #print(message.sid)