import os
import random
import pygame
from pygame.locals import *

pygame.init()

janela_inicial = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Início")

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
atacando = pygame.image.load(os.path.join(diretorio_imagens, 'sprite2.png')).convert_alpha()
caminhar_direita = pygame.image.load(os.path.join(diretorio_imagens, 'andar_direita.png')).convert_alpha()
caminhar_esquerda = pygame.image.load(os.path.join(diretorio_imagens, 'andar_esquerda.png')).convert_alpha()
parado_ = pygame.image.load(os.path.join(diretorio_imagens, 'parado.png')).convert_alpha()
sumindo = pygame.image.load(os.path.join(diretorio_imagens, 'sumir.png')).convert_alpha()
pedra = pygame.image.load(os.path.join(diretorio_imagens, 'pedras.png')).convert_alpha()
corrente = pygame.image.load(os.path.join(diretorio_imagens, 'corrente.png')).convert_alpha()
efeito = pygame.image.load(os.path.join(diretorio_imagens, 'caixa1.png')).convert_alpha()
efeito2 = pygame.image.load(os.path.join(diretorio_imagens, 'caixa2.png')).convert_alpha()
acesa = pygame.image.load(os.path.join(diretorio_imagens, 'acesa.png')).convert_alpha()
apagada = pygame.image.load(os.path.join(diretorio_imagens, 'apagada.png')).convert_alpha()
embaixo = pygame.image.load(os.path.join(diretorio_imagens, 'fundo_embaixo.png')).convert_alpha()

##########################################################################################################

# função que torna mais facil criar textos na tela
def texto(janela, msg, color, x, y, s, center=True):
  
    screen_text = pygame.font.SysFont("Calibri", s).render(msg, True, color)
    if center:
        rect = screen_text.get_rect()
        rect.center = (x, y) #centraliza o texto
    else:
        rect = (x, y)
    janela.blit(screen_text, rect)

##########################################################################################################

def desenha_botao(botao, janela, tela):
    if tela == "inicial":
        if botao == 1:
            texto(janela, "JOGAR", (0,0,0),400, 100, 40)
            texto(janela, "SAIR", (0,0,0), 400, 220, 30)
        
        elif botao == 2:
            texto(janela, "JOGAR", (0,0,0),400, 100, 30)
            texto(janela, "SAIR", (0,0,0), 400, 220, 40)

    elif tela == "escolhe tema":
        if botao == 1 or botao == 0:
            texto(janela, "Animais", (0,0,0),400, 100, 40)
            texto(janela, "Traduzir", (0,0,0), 400, 220, 30)
        
        elif botao == 2 or botao == 0:
            texto(janela, "Animais", (0,0,0),400, 100, 30)
            texto(janela, "Traduzir", (0,0,0), 400, 220, 40)
       
    pygame.display.flip()

##########################################################################################################

def fundo_inicial(janela, cinza):
    # fundo_inicial = pygame.image.load(os.path.join(diretorio_imagens,'plano_de_fundo.png'))
    # janela.blit(fundo_inicial, (0,0))
    janela.fill(cinza)
    

##########################################################################################################

def fundo_primeiro_nivel(janela, cinza):
    janela.fill(cinza)
    janela.blit(embaixo, (0,210))
    janela.blit(pedra, (0,210))
    janela.blit(pedra, (0,0))
    janela.blit(corrente, (0, 242))

##########################################################################################################

def tela_escolher(janela, cinza):
    janela.fill(cinza)


##########################################################################################################

def sorteia_palavra(arquivo):
    with open(arquivo, "rt") as f:
        linhas = f.readlines()
    return linhas[random.randint(0,len(linhas)-1)].strip()

##########################################################################################################

def some_letra(letra, lista):
    lista[letra][3] = False
    return lista

##########################################################################################################

def redefine_letras(lista):
    for i in range(26):
        if lista[i][3] == False:
            lista[i][3] = True
    return lista

##########################################################################################################

def desenha_letras(janela, li):
    for x, y, i, t in li:
        if t:
            janela.blit(i, (x, y))

##########################################################################################################

def dica(janela, palavra):
    texto(janela, ("Dica: "+palavra), (0,0,0), 200, 450, 40)

##########################################################################################################

def tela_ganhou(janela, cinza, palavra):
    janela.fill(cinza)
    texto(janela, ("Voce GANHOU, a palavra era: "), (0,0,0), 400, 100, 40)
    texto(janela, (palavra), (0,0,0), 300, 200, 40)
    texto(janela, ("Pressione enter para continuar"), (0,0,0), 300, 300, 40)

##########################################################################################################

def tela_perdeu(janela, cinza, palavra):
    janela.fill(cinza)
    texto(janela, ("Voce PERDEU, a palavra era: "), (0,0,0), 400, 100, 40)
    texto(janela, (palavra), (0,0,0), 300, 200, 40)
    texto(janela, ("Pressione enter para continuar"), (0,0,0), 300, 300, 40)
