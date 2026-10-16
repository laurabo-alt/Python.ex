n1 = float(input("Digite seu primeiro numero: "))
n2 = float(input("Digite seu segundo numero: "))
n3 = float(input("Digite seu terceiro numero: "))
#para o usario digitar três números

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

print(f"O maior é {maior:g}")