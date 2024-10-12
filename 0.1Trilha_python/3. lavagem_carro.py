from datetime import datetime, timedelta, date

tipo_carro = str(input("Informe o seu tipo de carro (P, M ou G): "))
tamanho = tipo_carro.upper()
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

data_atual = datetime.now()

while tamanho not in ["P", "M", "G"]:
    tipo_carro = str(input("Valor incorreto!! \nInforme novamente o seu tipo de carro (P, M ou G) ou pressione E para cancelar: "))
    tamanho = tipo_carro.upper()
    break

if tamanho == "E":
        print("Agradecemos o seu contato")
elif tamanho == "P":
        data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
        print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tamanho == "M":
        data_estimada = data_atual + timedelta(minutes=tempo_medio)
        print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else: 
        data_estimada = data_atual + timedelta(minutes=tempo_grande)
        print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

print(date.today() - timedelta(days=1)) #fazendo subtração de dias
data_agora = datetime.now() #descobrindo o dia e hora agora
resultado = data_agora - timedelta(hours =1) #fazendo subtração de horas
print(resultado.time()) #printando só hora
print(data_agora.date()) #printando só data