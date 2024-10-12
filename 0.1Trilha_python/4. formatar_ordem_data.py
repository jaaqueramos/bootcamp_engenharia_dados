from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a" #posso usar quanto quiser para mostrar.  %a é a semana correspondente
mascara_en = "%Y-%m-%d %H:%M"

print(type(data_hora_atual))

data_mascara = data_hora_atual.strftime(mascara_ptbr) #substituindo a hora atual pela máscara que criei, vai sair de datetime par string. Se quiser mostrar só dia funciona tbm
print(data_mascara)
print(type(data_mascara))


data_convertida = datetime.strptime(data_hora_str, mascara_en) #substituindo a string para formato de data
print(data_convertida)
print(type(data_convertida)) #vendo o tipo que está o dado
print(type(data_hora_str)) #vendo o tipo que está o dado

#documentação:https://docs.python.org/pt-br/3/library/datetime.html#strftime-and-strptime-behavior