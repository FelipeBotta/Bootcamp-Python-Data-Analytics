nome = "Luis Felipe"
idade = 24
profissao = "Programador de Materiais"
linguagem = "Java"
saldo = 45.435

dados = {"nome": "Luis Felipe", "idade": 24}

print("Nome:%s Idade:%d" %(nome,idade))

print("Nome:{} Idade:{}" .format(nome,idade))

print("Nome:{0} Idade:{1}" .format(nome,idade))

print("Nome:{1} Idade:{0}" .format(idade,nome))

print("Nome:{nome} Idade:{idade}" .format(nome=nome,idade=idade))

print("Nome:{name} Idade:{age}" .format(name=nome,age=idade))

print("Nome:{nome} Idade:{idade}" .format(**dados))

print(f"Nome:{nome} Idade:{idade}")

print(f"Nome:{nome} Idade:{idade} Saldo:{saldo:.2f}")