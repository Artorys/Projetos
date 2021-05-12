import pygame
import random
pygame.init()
imagem1 = pygame.image.load('maxresdefault.jpg')
imagem2 = pygame.image.load('index.jpeg')
imagem3 = pygame.image.load('res.jpeg')
lista = [imagem1, imagem2, imagem3]
imagens_aleatorias = random.choice(lista)
if imagens_aleatorias == imagem1:
    print(imagem1)
    print('QUE JOGO MERDA')
elif imagens_aleatorias == imagem2:
    print(imagem2)
    print('JOGO BOM')
elif imagens_aleatorias == imagem3:
    print(imagem3)
    print('QUE JOGO INCRÍVEL,COME O MEU CÚ POR FAVOR')


