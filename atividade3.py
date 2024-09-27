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
    # Checa se figura ultrapassa o topo ou base da janela
        # Figura atingiu o topo ou a base da janela
        # Se sim, então inverte o valor de velocidade. Efeito visual de quicar.
def mover (figura, dimensaoJanela):
    borda_esquerda = 0
    bola_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
    if figura['objRect'].top < borda_superior or figura['objRect'].bottom > borda _inferior:
        figura['vel'][1] = -figura['vel'][1]")