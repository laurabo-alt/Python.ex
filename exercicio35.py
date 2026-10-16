n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, * ou /): ")
#para o usuario digitar os dois numeros e escolher qual operação quer usar

if operador == "+":
    resultado = n1 + n2
    print(f"Resultado: {resultado:g}")
# se o usuario escolher adição

elif operador == "-":
    resultado = n1 - n2
    print(f"Resultado: {resultado:g}")
#se o usuario escolher subtração 

elif operador == "*":
    resultado = n1 * n2
    print(f"Resultado: {resultado:g}")
#se o usuario escolher multiplicação

elif operador == "/":
    if n2 == 0:
        print("Erro: divisão por zero")

else:
        resultado = n1 / n2
        print(f"Resultado: {resultado:g}")
#se o usuario escolher divisão

else:
    print("Operador inválido")