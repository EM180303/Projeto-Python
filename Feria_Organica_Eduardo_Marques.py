import os
import time

folhas = ('Alface americano', 'Alface crespa', 'Alho poró', 'Capim santo', 'Cebola', 'Cebolinha', 'Coentro', 'Couve folha', 'Chinguezay (acelga chinesa)', 'Espinafre', 'Hortelã', 'Salsinha', 'Rúcula')
preçoFolhas = (2.50, 2.50, 2.00, 2.50, 3.00, 2.50, 2.50, 2.50, 3.00, 3.00, 2.50, 2.50, 2.50)

frutas = ('Banana pacovan', 'Cana (Saquinho)', 'Laranja comum', 'Laranja mimo', 'Maracujá (1 Kg)')
preçoFrutas = (0.25, 2.00, 0.50, 0.50, 7.00)

raizes = ('Batata doce (1 Kg)', 'Cará (1 Kg)', 'Cenoura', 'Jerimum (1 Kg)', 'Macaxeira (1 Kg)', 'Rabanete', 'Quiabo')
preçoRaizes = (4.00, 5.00,  3.00, 5.00, 4.00, 2.50, 0.13)

outros = ('Fava seca (1 Kg)', 'Mel italiana (250 g)', 'Mel italiana (5 g)', 'Mel no favo (450 gramas)', 'Ovos de capoeira', 'Polpa de cajá (400 g)', 'Própolis (20 ml)', 'Pão com trigo (Pequeno)', 'Bolo (S / Trigo)', 'Bolinho de bacia (c / trigo)', 'Mini pizza', 'Pizza brotinho', 'Bolacha C / Trigo (Saquinho)', 'Sucos S / Açúcar (200 ml)', 'Sucos C / Açúcar (200 ml)', 'Sucos (1 litro)', 'Refeições congeladas (500 g)', 'Refeições congeladas (750 g)', 'Hambúrguer de ora-pro-nóbis', 'Molhos prontos', 'Massa artesanal')
preçoOutros = (12.00, 20.00, 35.00, 25.00, 1.00, 6.00, 16.00, 7.00, 10.00, 2.00, 3.00, 5.00, 5.00, 3.00, 3.00, 10.00, 12.00, 15.00, 2.00, 10.00, 12.00) 

pastinhas = ('Pepita de girassol', 'Homus de grão de bico com páprica', 'Bisnaga maionese de pepita girassol (250 ml)', 'Pimentas ao mel de engenho', 'Confit de tomatinho, Pimenta, Pimentão ou Berinjela', 'Geleia de tomate C / Pimenta, Abacaxi ou Manga', 'Caponata Siciliana')
preçoPastinhas = (5.00, 10.00, 10.00, 15.00, 15.00, 13.00, 13.00)

lanchesST = ('Quiche de macaxeira C / Alho poró', 'Quiche de macaxeira C / Tomate seco', 'Sanduiche S / Glúten de ricota', 'Sanduíche S / Glúten de caponata Siciliana', 'Sanduíche S / Glúten de ragu')
preçoLanchesST = (5.00, 5.00, 6.00, 6.00, 6.00)

lanchesCT = ('Empada de falso camarão', 'Empada de antepasto de berinjela', 'Empada de Tofu C / Cebola caramelizada', 'Pãozinhos de inhame recheados')
preçoLanchesCT = (5.00, 5.00, 5.00, 5.00)

formasPagamento = ('Dinheiro', 'Cartão de crédito', 'Cartão de débito')

carrinhoV = []
quantidade = 0
carrinhoP = []
continuar = True
carrinhoQ = []
total = 0

def exibir(x, y, z):
    print('-=' * 35)
    print('CÓDIGO   PRODUTO   VAlOR')
    print('*' * 70)
    for i in range(x):
        print(f'{i} - {y[i]} - R$ {z[i]}')
    print('*' * 70)
    print()
    time.sleep(1)

while continuar == True:   
    print('\tFOLHAS E HORTALIÇAS / O MOLHO(Nº0)')  
    exibir(len(folhas), folhas, preçoFolhas)

    print('\tFRUTAS(Nº1)')
    exibir(len(frutas), frutas, preçoFrutas)

    print('\tRAÍZES, TUBÉRCULOS, LEGUMES E AFINS(Nº2)')
    exibir(len(raizes), raizes, preçoRaizes)

    print('\tOUTROS(Nº3)')
    exibir(len(outros), outros, preçoOutros)

    print('\tPASTINHAS, ANTEPASTOS E GELEIAS(Nº4)')
    exibir(len(pastinhas), pastinhas, preçoPastinhas)

    print('\tLANCHES (sem trigo)(Nº5)')
    exibir(len(lanchesST), lanchesST, preçoLanchesST)

    print('\tLANCHES (com trigo)(Nº6)')
    exibir(len(lanchesCT), lanchesCT, preçoLanchesCT)

    nLista = int(input('Digite o número da lista em que o produto que você deseja se encontra: '))

    time.sleep(1)
    os.system("cls")

    def escolhaP (x,y):
        produto = int(input('Qual o código do produto que você deseja? '))
        quantidade = int(input(f'Quantos(a) {x[produto]} você deseja? '))
        valor = (quantidade * y[produto])
        print(f'Vai ficar R$ {valor}')
        carrinhoQ.append(quantidade)
        carrinhoV.append(valor)
        carrinhoP.append(x[produto])
        carrinhoAtual = sum(carrinhoV)
        print(f'Seu carrinho = {carrinhoAtual}')


    if nLista == 0:
        print('\tFOLHAS E HORTALIÇAS / O MOLHO(Nº0)')  
        exibir(len(folhas), folhas, preçoFolhas)
        escolhaP(folhas, preçoFolhas)
    elif nLista == 1:
        print('\tFRUTAS(Nº1)')
        exibir(len(frutas), frutas, preçoFrutas)
        escolhaP(frutas, preçoFrutas)
    elif nLista == 2:
        print('\tRAÍZES, TUBÉRCULOS, LEGUMES E AFINS(Nº2)')
        exibir(len(raizes), raizes, preçoRaizes)
        escolhaP(raizes, preçoRaizes)
    elif nLista == 3:
        print('\tOUTROS(Nº3)')
        exibir(len(outros), outros, preçoOutros)
        escolhaP(outros, preçoOutros)
    elif nLista == 4:
        print('\tPASTINHAS, ANTEPASTOS E GELEIAS(Nº4)')
        exibir(len(pastinhas), pastinhas, preçoPastinhas)
        escolhaP(pastinhas, preçoPastinhas)
    elif nLista == 5:
        print('\tLANCHES (sem trigo)(Nº5)')
        exibir(len(lanchesST), lanchesST, preçoLanchesST)
        escolhaP(lanchesST, preçoLanchesST)
    elif nLista == 6:
        print('\tLANCHES (com trigo)(Nº6)')
        exibir(len(lanchesCT), lanchesCT, preçoLanchesCT)
        escolhaP(lanchesCT, preçoLanchesCT)

    time.sleep(3)
    os.system("cls")
    
    pergunta = str(input('Deseja continuar comprando? {S para sim / N para não} '))
    pergunta = pergunta.upper()

    if pergunta == 'S':
        continuar = True
    elif pergunta == 'N':
        continuar = False
        print('Compra encerrada')

    time.sleep(2)
    os.system("cls")

nome = str(input('Qual o seu nome? '))
endereço = str(input('Qual seu endereço? '))
for i in range(3):
    print(f'{i} - Se for pagar em {formasPagamento[i]}')

pagamento = int(input('Qual forma de pagamento? {0/1/2} '))

print('Obrigado pela preferência, volte sempre!')

total = sum(carrinhoV)

with  open('Comprovante.txt', 'x', encoding = 'utf8') as arquivo:
    arquivo.write('\t\tCUPOM FISCAL\n')
    arquivo.write(50 * '-=')
    arquivo.write('\n')
    arquivo.write(f'Nome: {nome}\n')
    arquivo.write(f'Endereço: {endereço}\n')
    arquivo.write(f'Forma de pagamento: {formasPagamento[pagamento]}\n')
    arquivo.write('\n')
    arquivo.write('Nº - PRODUTO - QUANTIDADE - VALOR\n')
    arquivo.write(50 * '-=')
    arquivo.write('\n')
    for i in range(len(carrinhoP)):
        arquivo.write(f'{i+1} - {carrinhoP[i]} - {carrinhoQ[i]} - R$ {carrinhoV[i]}\n')
    arquivo.write('\n')
    arquivo.write(f'Total: R$ {total}')

os.system("cls")

arquivo = open('Comprovante.txt', encoding='utf8')
print(arquivo.read())
