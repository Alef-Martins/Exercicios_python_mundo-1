#Leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input("informe o valor do produto: "))
print(f'O valor do produto com 5% de desconto é {preco - (preco * 5 /100)}')