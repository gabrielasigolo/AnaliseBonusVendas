import pandas as pd # library que abre diversos arquivos
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC998b6403b41e0c72f70d7d0c6ad58701"
# Your Auth Token from twilio.com/console
auth_token  = "6db58029a07bcc40acc08aabc764505e"
client = Client(account_sid, auth_token)

# Abrir o seis arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any(): #Se algum valor naquela coluna é maior 55.000
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511989802317",
            from_="+13342343291",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

#Para cada arquivo:

# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

# Se for maior que 55.000 --> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada