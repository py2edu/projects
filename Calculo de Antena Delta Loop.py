print()
print('#' * 60)
print('{:^60}'.format('###       CALCULO DOS LADOS DA ANTENA DELTA LOOP!        ###'))
print('#' * 60)
print('-' * 60)
f = float(input('Digite a Frequência Central da Antena [em MHz]: '))
print('-' * 60)
Constante = 306
comprimento = 306 / f
print(f'O comprimento total é de {comprimento:.2f} m')
print('-' * 60)
lados = comprimento / 3
print(f'Serão 3 lados medindo {lados:.2f} m ')
print('-' * 60)
baloom = (comprimento / 4 * 0.66)
print(f'O comprimento do cabo de 75 ohms para baloom é de {baloom:.2f} m')
print('-' * 60)
print('#' * 60)
