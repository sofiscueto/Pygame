import pygame
import time

#Definindo as constantes de cores com o sistema RGB
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Definindo constante da dimensão da tela
#Usamos alguns nomes de variáveis em letras maiúsculas, pois queremos que estes valores sejam constantes, ou seja, em nenhum momento alteramos o valor destas variáveis.
LARGURAJANELA = 800
ALTURAJANELA = 700

#Definindo a função mover()
#figura: Será um dicionário
#dimensaoJanela: será uma tupla
def mover (figura, dimensaoJanela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dimensaoJanela[0]
    borda_inferior = dimensaoJanela[1]
    # Checa se figura ultrapassa o topo ou base da janela
    if figura['objRect'].top < borda_superior or figura['objRect'].bottom > borda_inferior:
        # Figura atingiu o topo ou a base da janela
        # Se sim, então inverte o valor de velocidade. Efeito visual de quicar.
        figura['vel'][1] = -figura['vel'][1]
# Checa se figura ultrapassa a esquerda ou à direita da janela
    if figura['objRect'].left < borda_esquerda or figura['objRect'].right> borda_direita:
        # Figura atingiu a esquerda ou à direita da janela
        # Se sim, então inverte o valor de velocidade. Efeito visual de quicar.
        figura['vel'][0] = -figura['vel'][0]
    # Finalmente, as novas coordenadas da figura correspondente serão, então, guardadas dentro da estrutura.
    figura['objRect'].x += figura['vel'][0]
    figura['objRect'].y += figura['vel'][1]

#Iniciando módulo de pygame
pygame.init()

#Criando a janela de tamanho conforme constante e com título "Animação"
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Animação")

#Criando as figuras
f1 = {"objRect": pygame.Rect(300, 80, 40, 80), "cor":VERMELHO, "vel":[0,-5], "forma":"ELIPSE"}
f2 = {"objRect": pygame.Rect(200, 200, 20, 20), "cor":VERDE, "vel":[5,5], "forma":"ELIPSE"}
f3 = {"objRect": pygame.Rect(100, 150, 60, 60), "cor":AZUL, "vel":[-5,5], "forma":"RETANGULO"}
f4 = {"objRect": pygame.Rect(200, 150, 80, 40), "cor":AMARELO, "vel":[5,0], "forma":"RETANGULO"}

figuras = [f1, f2, f3, f4]

pygame.display.update()
deve_continuar = True
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
    #preenchendo o fundo com a cor preta
    janela.fill(PRETO)

    for figura in figuras:
        # reposicionando a figura
        mover(figura,(LARGURAJANELA, ALTURAJANELA))

        # desenhando a figura na janela
        if figura["forma"] == "RETANGULO":
            pygame.draw.rect(janela, figura["cor"], figura["objRect"])

        elif figura["forma"] == "ELIPSE":
            pygame.draw.ellipse(janela, figura ["cor"], figura["objRect"])

    # atualizando na tela tudo o que foi desenhado
    pygame.display.update()

    #utilizando na tela tudo que foi desenhado
    time.sleep(0.02)

pygame.quit()