import pygame
import time

PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)

LARGURAJANELA = 800
ALTURAJANELA = 700

def mover (figura, dimensaoJanela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dimensaoJanela[0]
    borda_inferior = dimensaoJanela[1]
    
    if figura['objRect'].top < borda_superior or figura['objRect'].bottom > borda_inferior:
        figura['vel'][1] = -figura['vel'][1]

    if figura['objRect'].left < borda_esquerda or figura['objRect'].right> borda_direita:
        figura['vel'][0] = -figura['vel'][0]
    
    figura['objRect'].x += figura['vel'][0]
    figura['objRect'].y += figura['vel'][1]

pygame.init()

relogio = pygame.time.Clock()

janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Colisão")

#Criando as figuras
b1 = {"objRect": pygame.Rect(575, 80, 40, 40), "cor":VERMELHO, "vel":[0,2]}
b2 = {"objRect": pygame.Rect(275, 200, 40, 40), "cor":VERDE, "vel":[0,3]}
b3 = {"objRect": pygame.Rect(375, 150, 40, 40), "cor":AZUL, "vel":[0,1]}
b4 = {"objRect": pygame.Rect(175, 150, 40, 40), "cor":AMARELO, "vel":[0,4]}

blocos = [b1, b2, b3, b4]

bola = {"objRect": pygame.Rect(270, 330, 30, 30), "cor":BRANCO, "vel":[10,10]}

pygame.display.update()

deve_continuar = True

while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
    janela.fill(PRETO)

    for bloco in blocos:
        mover(bloco,(LARGURAJANELA, ALTURAJANELA))

        pygame.draw.rect(janela, bloco["cor"], bloco["objRect"])

        mudaCor = bola['objRect'].colliderect(bloco["objRect"])
        if mudaCor:
            bola["cor"] = bloco["cor"]

    mover(bola,(LARGURAJANELA, ALTURAJANELA))
    pygame.draw.ellipse(janela, bola["cor"], bola["objRect"])

    pygame.display.update()

    relogio.tick(40)

pygame.quit()