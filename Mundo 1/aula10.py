nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = nota1 + nota2 / 2
print(f'A sua média foi: {media:.1f}')
print(f'Sua média foi boa' if media > 6 else 'Sua média foi baixa')