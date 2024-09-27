import pygame 

#Definindo as constantes de cores com o sistema rgb
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Definindo constante com o valor de PI (Utilizando para o calculo na criação das figuras)
PI = 3.1416

# Inicializando os módulos do Pygame
pygame.init()

# Criando a janela de tamanho 800x600 e com título "Figuras e texto"
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Figuras e Texto")

# Utilizando método fill() para aplicar cor a superficie
janela.fill(BRANCO)

#A mudança de cor da superficie acima somente será aplicada quando rodar o código a baixo
pygame.display.update()

#É passado dois parâmetros sendo (Nome da fonte, Tamanho da fonte). Se passarmos None como argumento, será então usada a fonte padrão do sistema.
font_path = "Pygame/Raleway-Italic-VariableFont_wght.ttf"
fonte = pygame.font.Font(font_path ,48)

# Utilizando o método render() para renderizar o texto a apresentar na tela
#Os parâmetros passados em render é: (Texto a ser inserido, Se será suavizado, Cor do texto, Cor de fundo), cor de fundo sendo opcional
texto= fonte.render("Olá mundo!", True, BRANCO, AZUL)

#Utilizando o método blit() para desenhar o conteúdo na tela
#É passado dois parâmetros sendo (Texto a ser apresentado, posição em janela).Posição (Horizontal, Vertical]
janela.blit(texto, [30, 150])

#Utilizando o método line() para desenhar uma linha na tela
# É passado os seguintes parâmetros: (Janela, Cor da Linha, Ponto Inicial da linha, Ponto Final da linha, Espessura da linha).Posição [Horizontal, Vertical]
pygame.draw.line(janela, VERMELHO, [60, 300], [250, 300], 4)

# Utilizando o método polygon() para desenhar um poligono na tela
#É passado os seguintes parâmetros:(Janela, Cor, Coordenadas dos vértices, Largura da linha).Posição [Horizontal, Vertical]
pygame.draw.polygon(janela, PRETO,([191, 206], [236, 277], [156, 277]), 0)

# Utilizando o método circle() para desenhar um círculo na tela 
#É passado os seguintes parâmetros:(Janela, Cor, Coordenadas do centro, Raio do círculo em pixels, Largura da linha).Posição [Horizontal, Vertical]
pygame.draw.circle(janela, VERDE, (300, 500), 50, 0)

# Utilizando o método ellipse() para desenhar uma elipse na tela 
#É passado os seguintes parâmetros:(Janela, Cor, Coordenadas (Esquerda, Topo, Largura, Altura), Largura da linha).Posição [Horizontal, Vertical]
pygame.draw.ellipse(janela, VERMELHO, (400, 300, 120, 120), 1)

# Utilizando o método rect() para desenhar um retângulo na tela
#É passado os seguintes parâmetros:(Janela, Cor, Coordenadas (Esquerda, Topo, Largura, Altura), Largura da linha).Posição (Horizontal, Vertical]
pygame.draw.rect(janela, VERDE, (20, 20, 60, 40), 0)

#Utilizando o método arc() para desenhar um arco na tela
#É passado os seguintes parâmetros:(Janela, Cor, Coordenadas (Esquerda, Topo, Largura, Altura), Angulo Inicial, Angulo final, Largura da linha).Posição [Horizontal, Vertical)
pygame.draw.arc(janela, VERMELHO, (250, 75, 150, 125), PI/2, 3 * PI, 2)

pygame.draw.arc(janela, AZUL, (250, 75, 150, 125), -PI/2, PI/2, 2)


pygame.display.update()

deve_continuar = True

while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False

#Fechar os módulos de pygame
pygame.quit()