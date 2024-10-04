import pygame, random

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)

LARGURAJANELA = 700
ALTURAJANELA = 600
VEL = 6
INTERACOES = 30
TAMANHOBLOCO = 20

def moverJogador(jogador, teclas, dimensaoJanela):
    bordaEsquerda = 0
    bordaSuperior = 0
    bordaDireita = dimensaoJanela[0]
    bordaInferior = dimensaoJanela[1]

    if teclas["esquerda"] and jogador["objRect"].left > bordaEsquerda:
        jogador["objRect"].x -= jogador["vel"]
    
    if teclas["direita"] and jogador["objRect"].right < bordaDireita:
        jogador["objRect"].x += jogador["vel"]

    if teclas["cima"] and jogador["objRect"].top > bordaSuperior:
        jogador["objRect"].y -= jogador["vel"]

    if teclas["baixo"] and jogador["objRect"].bottom < bordaInferior:
        jogador["objRect"].y += jogador["vel"]

def moverBloco(bloco):
    bloco["objRect"].y += bloco ["vel"]

pygame.init()

relogio = pygame.time.Clock()

janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Teclado e Mouse")

jogador = {"objRect": pygame.Rect(300, 100, 50, 50), "cor": VERDE, "vel": VEL}

teclas = {"esquerda": False, "direita": False, "cima": False, "baixo": False,}

contador = 0
blocos = []
deve_continuar = True

while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

    teclas = pygame.key.get_pressed()
    teclas = {
        "esquerda": teclas[pygame.K_LEFT] or teclas[pygame.K_a],
        "direita": teclas[pygame.K_RIGHT] or teclas[pygame.K_d],
        "cima": teclas[pygame.K_UP] or teclas[pygame.K_w],
        "baixo": teclas[pygame.K_DOWN] or teclas[pygame.K_s],
    }

    if evento.type == pygame.MOUSEBUTTONDOWN:
        blocos.append({"objRect": pygame.Rect(evento.pos[0], evento.pos[1], TAMANHOBLOCO, TAMANHOBLOCO), "cor": BRANCO, "vel": 1})

    contador += 1
    if contador >= INTERACOES:
        contador = 0
        posX = random.randint(0, (LARGURAJANELA -TAMANHOBLOCO))
        posY = -TAMANHOBLOCO 
        velRandom = random.randint(1, (VEL + 3))
        blocos.append({"objRect": pygame.Rect(posX, posY, TAMANHOBLOCO, TAMANHOBLOCO), "cor": BRANCO, "vel": velRandom})

    janela.fill(PRETO)

    moverJogador(jogador, teclas, (LARGURAJANELA, ALTURAJANELA))

    pygame.draw.rect(janela, jogador["cor"], jogador["objRect"])

    for bloco in blocos:
        bateu = jogador["objRect"].colliderect(bloco["objRect"])
        if bateu or bloco["objRect"].y > ALTURAJANELA:
            blocos.remove(bloco)

    for bloco in blocos:
        moverBloco(bloco)
        pygame.draw.rect(janela, bloco["cor"], bloco["objRect"])


    pygame.display.update()

    relogio.tick(40)

pygame.quit()