import pygame
import random
from PIL import Image


IMAGENS_COMIDA = {
    'banana': pygame.image.load('C:\VSC\imagens/banana.png'),
    'morango': pygame.image.load('C:\VSC\imagens/morango.png'),
    'pera': pygame.image.load('C:\VSC\imagens/pera.png')
}


# inicializa o Pygame
pygame.init()

# define as dimensões da tela
tela_largura = 800
tela_altura = 600

# cria a tela
tela = pygame.display.set_mode((tela_largura, tela_altura))

# define as cores usadas no jogo
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# define o tamanho da cobra e o tamanho do quadrado do jogo
tamanho_cobra = 1
tamanho_quadrado = 5

# define a posição inicial da cobra
cabeca_cobra = [tela_largura/2, tela_altura/2]
corpo_cobra = [[cabeca_cobra[0], cabeca_cobra[1]+i*tamanho_quadrado] for i in range(3)]

# define a posição inicial da comida
posicao_comida = [random.randrange(1, tela_largura/tamanho_quadrado)*tamanho_quadrado,
                  random.randrange(1, tela_altura/tamanho_quadrado)*tamanho_quadrado]

# define a direção inicial da cobra
direcao_cobra = 'UP'

# Cria a aba vermelha
aba = pygame.Surface((tela_largura, 30))
aba.fill(vermelho)

# definições
pontos = 0
vidas = 5
reset_snak = False


# Define a fonte que será usada para o texto
fonte = pygame.font.SysFont("calibri", 15)

# Mostra a Pontuação
def mostrar_pontuacao(pontos):
    texto = fonte.render("Pontuação: {}".format(pontos), True, preto)
    tela.blit(texto, (0, 10))

# Define a função que será usada para exibir as vidas na tela
def vidas_qtde(qtde_vidas):
    texto = fonte.render("Vidas: " + str(qtde_vidas), True, preto)
    tela.blit(texto, [0, 0])

# Define a função que será usada para exibir mensagens na tela
def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [tela_largura / 6, tela_altura / 3])

# define a função para desenhar a cobra e a comida na tela
def desenhar_cobra_e_comida():
    tela.fill(preto)
    for posicao in corpo_cobra:
        pygame.draw.rect(tela, branco, [posicao[0], posicao[1], tamanho_quadrado, tamanho_quadrado])
    pygame.draw.rect(tela, verde, [posicao_comida[0], posicao_comida[1], tamanho_quadrado, tamanho_quadrado])
    vidas_qtde(vidas)
    mostrar_pontuacao(pontos) 
    pygame.display.update()

#desenhar a comida
def gerar_posicao_comida():
    global posicao_comida
    posicao_comida = [random.randrange(1, tela_largura/tamanho_quadrado)*tamanho_quadrado,
                          random.randrange(1, tela_altura/tamanho_quadrado)*tamanho_quadrado]

# define a função para verificar se a cobra comeu a comida
def verificar_comida():
    global posicao_comida, corpo_cobra, pontos
    if cabeca_cobra == posicao_comida:
        pontos += 1
        gerar_posicao_comida()
        corpo_cobra.append(corpo_cobra[-1])
        print("Pontos: ", pontos)
  
  
def reset_jogo():
    # definir as variáveis como no início do jogo
    global cabeca_cobra, corpo_cobra, pos_comida, direcao_cobra, pontos, vidas
    cabeca_cobra = [tela_largura // 2, tela_altura // 2]
    corpo_cobra = [[cabeca_cobra[0], cabeca_cobra[1]+i*tamanho_quadrado] for i in range(3)]
    pos_comida = gerar_posicao_comida()
    direcao_cobra = 'RIGHT'
    pontos = 0
    vidas -= 1
    # desenhar a mensagem "Você perdeu uma vida"
    fonte = pygame.font.SysFont(None, 50)
    mensagem = fonte.render("Você perdeu uma vida", True, vermelho)
    pos_mensagem = mensagem.get_rect(center=(tela_largura/2, tela_altura/2))
    tela.blit(mensagem, pos_mensagem)
    # atualizar a tela
    pygame.display.update()
    # esperar um pouco para o jogador ver a mensagem
    pygame.time.wait(1000)
 
        
# define a função para verificar se a cobra colidiu com as paredes ou com o próprio corpo
def verificar_colisao():
    global corpo_cobra, vidas
    if cabeca_cobra[0] < 0 or cabeca_cobra[0] > tela_largura-tamanho_quadrado or \
            cabeca_cobra[1] < 0 or cabeca_cobra[1] > tela_altura-tamanho_quadrado:       
        reset_jogo()
        return True
    for posicao in corpo_cobra[1:]:
        if cabeca_cobra == posicao:
            reset_jogo()
            return True
    return False

def game_over_q():
     # Fim do jogo
    tela.fill((0, 0, 0))
    fonte = pygame.font.SysFont('calibri', 50)
    mensagem = fonte.render('Fim de jogo!', True, (255, 255, 255))
    tela.blit(mensagem, (tela_largura // 2 - mensagem.get_width() // 2,
                            tela_altura // 2 - mensagem.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(600)
    pygame.quit()

import pygame

def menu(screen_width, screen_height):
    pygame.init()
    
    # Definir a fonte e o tamanho
    font = pygame.font.SysFont('comicsansms', 40)

    # Criar as opções do menu
    new_game_text = font.render('Novo jogo', True, vermelho)
    high_score_text = font.render('Pontuação máxima', True, vermelho)
    about_text = font.render('Sobre', True, vermelho)
    quit_text = font.render('Sair do jogo', True, vermelho)
    
    
    
    # Definir a posição dos textos no menu
    new_game_rect = new_game_text.get_rect(center=(screen_width/2, screen_height/2 - 60))
    high_score_rect = high_score_text.get_rect(center=(screen_width/2, screen_height/2))
    about_rect = about_text.get_rect(center=(screen_width/2, screen_height/2 + 60))
    quit_rect = quit_text.get_rect(center=(screen_width/2, screen_height/2 + 120))

    # Definir a janela do menu
    menu_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Jogo da Cobra')

    # Loop do menu
    while True:
        # Definir o fundo do menu
        menu_screen.fill(branco)

        # Adicionar os textos das opções ao menu
        menu_screen.blit(new_game_text, new_game_rect)
        menu_screen.blit(high_score_text, high_score_rect)
        menu_screen.blit(about_text, about_rect)
        menu_screen.blit(quit_text, quit_rect)
        menu_screen.blit(IMAGENS_COMIDA['banana'], (50, 50))
        # Atualizar a janela do menu
        pygame.display.update()

        # Loop para verificar as interações do usuário
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if new_game_rect.collidepoint(mouse_pos):
                    return 'new_game'
                elif high_score_rect.collidepoint(mouse_pos):
                    return 'high_score'
                elif about_rect.collidepoint(mouse_pos):
                    return 'about'
                elif quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()



# define o loop principal do jogo
game_over = False
clock = pygame.time.Clock()

if menu(tela_largura, tela_altura) == "high_score":
    mensagem("maxima score",vermelho)
elif menu(tela_largura, tela_altura) == "about":
    mensagem("Fui eu que fiz",vermelho)
elif menu(tela_largura, tela_altura) == "new_game":   
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direcao_cobra != 'DOWN':
                    direcao_cobra = 'UP'
                elif event.key == pygame.K_DOWN and direcao_cobra != 'UP':
                    direcao_cobra = 'DOWN'
                elif event.key == pygame.K_LEFT and direcao_cobra != 'RIGHT':
                    direcao_cobra = 'LEFT'    
                elif event.key == pygame.K_RIGHT and direcao_cobra != 'LEFT':
                    direcao_cobra = 'RIGHT'  
                    
        # move a cobra na direção selecionada
        if direcao_cobra == 'UP':
            cabeca_cobra[1] -= tamanho_quadrado
        elif direcao_cobra == 'DOWN':
            cabeca_cobra[1] += tamanho_quadrado
        elif direcao_cobra == 'LEFT':
            cabeca_cobra[0] -= tamanho_quadrado
        elif direcao_cobra == 'RIGHT':
            cabeca_cobra[0] += tamanho_quadrado

        # atualiza a posição do corpo da cobra
        corpo_cobra.insert(0, list(cabeca_cobra))
        corpo_cobra.pop()

        # desenha a cobra e a comida na tela
        desenhar_cobra_e_comida()

        # verifica se a cobra comeu a comida
        verificar_comida()

        # verifica se a cobra colidiu com as paredes ou com o próprio corpo
        verificar_colisao()
                    
        if vidas == 0:
            game_over_q()

        # define a taxa de atualização do jogo
        clock.tick(15)
elif menu(tela_largura, tela_altura) == "quit":
    # encerra o Pygame
    pygame.quit()
