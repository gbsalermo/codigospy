#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra 'A'
#em que posição ela aparece a primeira vez e em que posicão ela aparece a ultima vez

frase = str(input("Give me a phrase: ")).strip() #Peço a frase como string e depois coloco .strip() para retirar os primeiros espaços
F = frase.upper() #deixo a frase totalmente maiuscula para evitar A's minusculos que possam não ser contabilizados
print('The totally of "a" on your phrase: {} ' .format(F.count('A'))) # uso o .count para contar a quantidade de repetições
print('The first position where be "a" is: {}' .format(F.find('A') + 1)) # uso o .find para encontrar a primeira aparição da letra
print('The last position where be "a" is: {}' .format(F.rfind('A') + 1)) # uso o .rfind(note que existe um r ali) para encontra a ultima aparição
