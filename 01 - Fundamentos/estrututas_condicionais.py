MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar sua CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas nao pode fazer as praticas")
else:
    print("Ainda nao pode tirar a CNH.")

