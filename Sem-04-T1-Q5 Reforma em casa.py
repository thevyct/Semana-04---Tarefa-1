altura = int(input())
comprimento = int(input())
largura = int(input())
areapiso = largura * comprimento
volumesala = largura * comprimento * altura
paredesala = 2 * altura * largura + 2 * altura * comprimento
print(f'{areapiso}')
print(f'{volumesala}')
print(f'{paredesala}')