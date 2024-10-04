import pygame, random

# Carregando as imagens.
imagemHarry = pygame.image.load("img/harry.png")
imagemDementador = pygame.image.load("img/dementador.png")
imagemRaio = pygame.image.load("img/lazer.png")
imagemFundo = pygame.image.load("img/fundo.jpg")

# Carregando constantes
LARGURAJANELA = 1920
ALTURAJANELA = 1000
CORTEXTO = (255, 255, 255) # Branco
QPS = 40 # quadros por segundo
TAMMINIMO = 10 # tamanho mínimo do dementador
TAMMAXIMO = 40 # tamanho máximo do dementador
VELMINIMA = 1 # velocidade mínima do dementador
VELMAXIMA = 8 # velocidade máxima do dementador
ITERACOES = 6 # número de iterações antes de criar um novo dementador
VELJOGADOR = 5 # velocidade de Harry
VELRAIO = (0,-20) # velocidade do raio

LARGURAHARRY = 80
ALTURAHARRY = 90
LARGURARAIO = 20
ALTURARAIO = 30

# Redimensionando as imagens
imagemFundo = pygame.transform.scale(imagemFundo, (LARGURAJANELA, ALTURAJANELA))
imagemHarry = pygame.transform.scale(imagemHarry, (LARGURAHARRY, ALTURAHARRY))
imagemRaio = pygame.transform.scale(imagemRaio, (LARGURARAIO, ALTURARAIO))

# Definindo a função moverJogador
def moverJogador(jogador, teclas, dimensaoJanela):
    bordaEsquerda = 0
    bordaSuperior = 0
    bordeDireita = dimensaoJanela[0]
    bordaInferior = dimensaoJanela[1]
    if teclas["esquerda"] and jogador["objRect"].left > bordaEsquerda:
        jogador["objRect"].x -= jogador["vel"]
    if teclas["direita"] and jogador["objRect"].right < bordeDireita:
        jogador["objRect"].x += jogador["vel"]
    if teclas["cima"] and jogador["objRect"].top > bordaSuperior:
        jogador["objRect"].y -= jogador["vel"]
    if teclas["baixo"] and jogador["objRect"].bottom < bordaInferior:
        jogador["objRect"].y += jogador["vel"]

def moverElemento(elemento):
    elemento["objRect"].x += elemento["vel"][0]
    elemento["objRect"].y += elemento["vel"][1]

def terminar():
    pygame.quit()
    exit()

def aguardarEntrada():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    terminar()
                return

def colocarTexto(texto, fonte, janela, x, y):
    objTexto = fonte.render(texto, True, CORTEXTO)
    rectTexto = objTexto.get_rect()
    rectTexto.topleft = (x, y)
    janela.blit(objTexto, rectTexto)

# Configurando pygame, relogio, janela.
pygame.init()
relogio = pygame.time.Clock()

# Criando janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Harry Potter A Batalha")

pygame.mouse.set_visible(False)
imagemFundoRedim = pygame.transform.scale(imagemFundo,(LARGURAJANELA, ALTURAJANELA))

# Configurando a fonte.
fonte = pygame.font.Font(None, 48)

# Configurando o som.
somFinal = pygame.mixer.Sound("mp3/vitoria.mp3")
somRecorde = pygame.mixer.Sound("mp3/recorde.mp3")
somTiro = pygame.mixer.Sound("mp3/magia.mp3")
pygame.mixer.music.load("mp3/musica-fundo.mp3")

# Tela de inicio.
colocarTexto("Dementadores", fonte, janela, LARGURAJANELA / 5, ALTURAJANELA / 3)
colocarTexto("Pressione uma tecla para começar.", fonte, janela, LARGURAJANELA / 20, ALTURAJANELA / 2)
pygame.display.update()

aguardarEntrada()

recorde = 0
while True:
    dementadores = []
    raios = []
    pontuacao = 0
    deve_continuar = True

    teclas = {"esquerda": False, "direita": False, "cima": False, "baixo": False}
    contador = 0
    pygame.mixer.music.play(-1, 0.0)

    posX = LARGURAJANELA / 2 - LARGURAHARRY / 2 
    posY = ALTURAJANELA - ALTURAHARRY - 50
    jogador = {"objRect": pygame.Rect(posX, posY, LARGURAHARRY, ALTURAHARRY), "imagem": imagemHarry, "vel": VELJOGADOR}

    while deve_continuar:
        pontuacao += 1
        if pontuacao == recorde:
            somRecorde.play()

        # Checando os eventos ocorridos.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    terminar()
                if evento.key == pygame.K_SPACE:
                    raio = {"objRect": pygame.Rect(jogador["objRect"].centerx, jogador["objRect"].top, LARGURARAIO, ALTURARAIO), "imagem": imagemRaio, "vel": VELRAIO}
                    raios.append(raio)
                    somTiro.play()
            if evento.type == pygame.MOUSEMOTION:
                centroX_jogador = jogador["objRect"].centerx
                centroY_jogador = jogador["objRect"].centery
                jogador["objRect"].move_ip(evento.pos[0] - centroX_jogador, evento.pos[1] - centroY_jogador)
            if evento.type == pygame.MOUSEBUTTONDOWN:
                raio = {"objRect": pygame.Rect(jogador["objRect"].centerx, jogador["objRect"].top, LARGURARAIO, ALTURARAIO), "imagem": imagemRaio, "vel": VELRAIO}
                raios.append(raio)
                somTiro.play()

        teclas = pygame.key.get_pressed()
        teclas = {
            "esquerda": teclas[pygame.K_LEFT] or teclas[pygame.K_a], "direita": teclas[pygame.K_RIGHT] or teclas[pygame.K_d],
            "cima": teclas[pygame.K_UP] or teclas[pygame.K_w], "baixo": teclas[pygame.K_DOWN] or teclas[pygame.K_s],
        }

        # Preenchendo o fundo da janela com a imagem correspondente.
        janela.blit(imagemFundoRedim, (0, 0))
        colocarTexto("Pontuação: " + str(pontuacao), fonte, janela, 10, 0)
        colocarTexto("Recorde: " + str(recorde), fonte, janela, 10, 40)

        # Adicionando dementador quando indicado.
        contador += 1
        if contador >= ITERACOES:
            contador = 0
            tamDementador = random.randint(TAMMINIMO, TAMMAXIMO)
            posX = random.randint(0, LARGURAJANELA - tamDementador)
            posY = - tamDementador
            vel_x = random.randint(-1, 1)
            vel_y = random.randint(VELMINIMA, VELMAXIMA)
            dementador = {"objRect": pygame.Rect(posX, posY, tamDementador, tamDementador), "imagem": pygame.transform.scale(imagemDementador, (tamDementador, tamDementador)), "vel": (vel_x, vel_y)}
            dementadores.append(dementador)

        # Movimentando e desenhando os dementador.
        for dementador in dementadores:
            moverElemento(dementador)
            janela.blit(dementador["imagem"], dementador["objRect"])

        # Eliminando os dementador que passam pela base da janela.
        for dementador in dementadores:
            if dementador["objRect"].top > ALTURAJANELA:
                dementadores.remove(dementador)

        # Movimentando e desenhando os raios.
        for raio in raios:
            moverElemento(raio)
            janela.blit(raio["imagem"], raio["objRect"])
        
        # Eliminando os raios que passam pelo topo da janela.
        for raio in raios[:]:  # Use uma cópia da lista para evitar problemas ao remover
            if raio["objRect"].bottom < 0:
                raios.remove(raio)

        # Movimentando e desenhando jogador(Harry).
        moverJogador(jogador, teclas, (LARGURAJANELA, ALTURAJANELA))
        janela.blit(jogador["imagem"], jogador["objRect"])

        # Checando se jogador ou algum raio colidiu com algum dementador.
        for dementador in dementadores:  # Use uma cópia da lista para evitar problemas ao remover
            jogadorColidiu = jogador["objRect"].colliderect(dementador["objRect"])
            if jogadorColidiu:
                if pontuacao > recorde:
                    recorde = pontuacao
                deve_continuar = False  # O jogo termina se a Harry colidir com um dementador
                break  # Não precisamos verificar mais, pois o jogo já acabou

            for raio in raios:  # Use uma cópia da lista para evitar problemas ao remover
                raioColidiu = raio["objRect"].colliderect(dementador["objRect"])
                if raioColidiu:
                    raios.remove(raio)
                    dementadores.remove(dementador)
                    break  # Saia do loop assim que encontrar uma colisão

        pygame.display.update()
        relogio.tick(QPS)

    # Parando o jogo e mostrando a tela final.
    pygame.mixer.music.stop()
    somFinal.play()
    colocarTexto("GAME OVER", fonte, janela, (LARGURAJANELA / 3), (ALTURAJANELA / 3))
    colocarTexto("Pressione uma tecla para jogar.", fonte, janela, (LARGURAJANELA / 10), (ALTURAJANELA / 2))
    pygame.display.update()

    # Aguardando entrada por teclado para reiniciar o jogo ou sair.
    aguardarEntrada()
    somFinal.stop()
