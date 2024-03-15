texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando a funcao iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra,end="")
else:
    print()
    print("Executa o final do laco")




# Exemplo utilizando a funcao range
for numero in range(0,51,5):
    print(numero,end=" ")
