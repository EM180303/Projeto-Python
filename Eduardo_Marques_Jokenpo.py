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
rodada = []
rodada.append('x')
rodada.append(0)
rodada.append(0)
vencedor = False

print('***Bem vindos!***')
print('Preparados para o Jokenpo? Sim?')
# para que o nome do jogador 1 fique na lista com o indice 1 e o nome do jogador 2 no 2
nome.append('x')
nome.append(str(input('Então informe o nome do jogador 1: ')))
nome.append(str(input('Agora o nome do jogador 2: ')))

print('\n Quem vencer 2  rodadas primeiro ganha')

time.sleep(2)
os.system("cls")

for cont in [1, 2]:
 print('Somente ', nome[cont], ' pode ver apartir de agora \n')
 for i in [1, 2, 3]:
   print('Digite ',i,' para escolher ',jokenpo[i])
 escolha.append(int(input()))
 print('Você escolheu ',jokenpo[escolha[cont]])

 time.sleep(2)
 os.system("cls")

if (escolha[1] == escolha[2]):
    print('Empate')
elif (((escolha[1] == 1) and (escolha[2] == 3)) or ((escolha[1] == 2) and (escolha[2] == 1)) or ((escolha[1] == 3) and (escolha[2] == 2))): 
    print(nome[1],' ganhou essa rodada')
    rodada[1] += 1
elif (((escolha[2] == 1) and (escolha[1] == 3)) or ((escolha[2] == 2) and (escolha[1] == 1)) or ((escolha[2] == 3) and (escolha[1] == 2))): 
    print(nome[1],' ganhou essa rodada')
    rodada[2] += 1

if ((rodada[1] == 2) or (rodada[2] == 1)):
    vencedor = True
else:
    vencedor = False

