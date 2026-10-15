nome = input("Digite o nome do aluno: ")
#para o usuario digitar o nome do aluno

nota1 = float(input("digite a sua primeira nota"))
nota2 = float(input("digite a sua segunda nota"))

media = (nota1 + nota2) / 2

if media >= 7:
    print("média:", media, "aprovada")

else:
    print("média", media, "reprovado")