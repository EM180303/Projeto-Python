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
preçoLancheCT = (5.00, 5.00, 5.00, 5.00)

carrinho = []
carrinhoV = 0

print('\tFOLHAS E HORTALIÇAS / O MOLHO(Nº0)')

def exibir(x, y, z):
    print('-=' * 25)
    print('CÓDIGO   PRODUTO   VAlOR')
    print('*' * 50)
    for i in range(x):
        print(f'{i} - {y[i]} - R$ {z[i]}')
    print('*' * 50)
    print()
    

exibir(len(folhas), folhas, preçoFolhas)

print('\t\tFRUTAS(Nº1)')
exibir(len(frutas), frutas, preçoFrutas)

print('    RAÍZES, TUBÉRCULOS, LEGUMES E AFINS(Nº2)')
exibir(len(raizes), raizes, preçoRaizes)

print('\t\tOUTROS(Nº3)')
exibir(len(outros), outros, preçoOutros)

print('     PASTILHAS, ANTEPASTOS E GELEIAS(Nº4)')
exibir(len(pastinhas), pastinhas, preçoPastinhas)

print('\tLANCHES (sem trigo)(Nº5)')
exibir(len(lanchesST), lanchesST, preçoLanchesST)

print('\tLANCHES (com trigo)(Nº6)')
exibir(len(lanchesCT), lanchesCT, preçoLancheCT)









