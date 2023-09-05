
op = int(input("Qual a operação que deseja?\nSoma [1]\nsubtração [2]\nmultiplicação [3]\ndivisão [4]\nDigite o numero da operação:"))

if op == 1:
    print("Ótimo, você escolheu a opção de soma")
    n1 = int(input("Agora, digite o primeiro valor para a operação: "))
    n2 = int(input("Agora, digite o primeiro valor para a operação: "))
    print("O valor de {} + {} totaliza {}" .format(n1, n2, n1 + n2))
elif op == 2:
    print("Ótimo, você escolheu a opção de subtração")
    n1 = int(input("Agora, digite o primeiro valor para a operação: "))
    n2 = int(input("Agora, digite o primeiro valor para a operação: "))
    print("O valor de {} - {} totaliza {}" .format(n1, n2, n1 - n2))

elif op == 3:
    print("Ótimo, você escolheu a opção de multiplicação")
    n1 = int(input("Agora, digite o primeiro valor para a operação: "))
    n2 = int(input("Agora, digite o primeiro valor para a operação: "))
    print("O valor de {} * {} totaliza {}" .format(n1, n2, n1 * n2))

elif op == 4:
    print("Ótimo, você escolheu a opção de divisão")
    n1 = int(input("Agora, digite o primeiro valor para a operação: "))
    n2 = int(input("Agora, digite o primeiro valor para a operação: "))
    print("O valor de {} / {} totaliza {}" .format(n1, n2, n1 / n2))
else:
    print("Por gentileza escolha uma opção válida")



