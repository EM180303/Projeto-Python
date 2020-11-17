import os
import time
nome = []
jokenpo = []
jokenpo.append('x')
jokenpo.append('Pedra')
jokenpo.append('Papel')
jokenpo.append('Tesoura')
escolha = []
escolha.append('x')

print('***Bem vindos!***')
print('Preparados para o Jokenpo? Sim?')
# para que o nome do jogador 1 fique na lista com o indice 1 e o nome do jogador 2 no 2
nome.append('x')
nome.append(str(input('Então informe o nome do jogador 1: ')))
nome.append(str(input('Agora o nome do jogador 2: ')))

time.sleep(1)
os.system("cls")

for cont in [1, 2]:
 print('Somente ', nome[cont], ' pode ver apartir de agora ')
 print('')
 for i in [1, 2, 3]:
   print('Digite ',i,' para escolher ',jokenpo[i])
 escolha.append(int(input()))
 print('Você escolheu ',jokenpo[escolha[cont]])

 time.sleep(2)
 os.system("cls")
