import os
import random
import pygame
from funcoes import *
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
ifem = pygame.image.load(os.path.join(diretorio_imagens, 'ifem.png')).convert_alpha()
embaixo = pygame.image.load(os.path.join(diretorio_imagens, 'fundo_embaixo.png')).convert_alpha()
##############################################################################################

class Forca:
    def __init__(self, palavra, janela):
        self.palavra = palavra
        self.janela = janela
        self.minuscula = self.palavra.lower()
        self.ja_usadas = []
        self.letras_certas = []
        self.letras_palavra = [x for x in self.minuscula]
        self.xl = 300
        self.erros = 0
        self.ultima_letra = ""
        self.lista_letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",""]
    
    def tem_letra(self, letra):
        self.letra = letra
        if self.letra not in self.ja_usadas and self.letra != '' and self.letra != self.ultima_letra: 
            self.ja_usadas.append(self.letra)
            if self.letra in self.letras_palavra and self.letra != self.ultima_letra:
                self.letras_certas.append(self.letra)
            elif self.letra not in self.letras_palavra and self.letra != '' and self.letra != self.ultima_letra:
                self.erros += 1
            self.ultima_letra = self.letra

    def desenha(self, imagens):
        self.xl = 97
        self.xls = 97
        self.cont = 0
        self.teste = True
        for l in self.letras_palavra:
            if l not in self.ja_usadas and l != "-":
                self.cont += 1
                if self.cont == len(self.letras_palavra):
                    self.janela.blit(efeito2, (self.xls, 370))
                    self.cont = 0
                else:
                    self.janela.blit(efeito, (self.xls, 370))
                self.xl += 35
                self.xls += 35
                self.teste = False

            if l == "-":
                self.cont += 1
                if self.cont == len(self.letras_palavra):
                    self.janela.blit(efeito2, (self.xls, 370))
                    self.cont = 0
                else:
                    self.janela.blit(efeito, (self.xls, 370))
                self.janela.blit(ifem, (self.xl, 370))
                self.xl += 35
                self.xls += 35

            if l in self.ja_usadas:
                self.cont += 1
                if self.cont == len(self.letras_palavra):
                    self.janela.blit(efeito2, (self.xls, 370))
                    self.cont = 0
                else:
                    self.janela.blit(efeito, (self.xls, 370))
                self.janela.blit(imagens[self.lista_letras.index(l)][2], (self.xl+3, 373))
                self.xl += 35
                self.xls += 35
    
    def ganhou(self):
        if len(self.letras_certas) > 0:
            return self.teste
        else: 
            return False

    def perdeu(self):
        if self.erros >= 6:
            self.letras_certas = []
            self.ja_usadas = []
            self.erros = 0
            return True
        else: return False

    def vidas(self, lampadas):
        self.lampadas = lampadas
        n = self.erros
        x = 50
        for i in range(6):
            if n > 0:
                n -= 1
                self.janela.blit(self.lampadas[0], (x, 32))
                x += 32
            else:
                self.janela.blit(self.lampadas[1], (x, 32))
                x += 32
    def define_letra(self):
        self.letra = 26
##############################################################################################

##############################################################################################

class Personagens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 860
        self.y = 200
        self.indice_matriz = 0
        
        self.letra = -1
        self.posicao_soco = -1
        self.muda_tela = False

        #matriz de imagens
        self.matriz = []

        #parado
        self.lista_parado = []
        for i in range(18):
            img = parado_.subsurface((i*128,0), (128,128))
            self.lista_parado.append(img)
        self.index_lista = 0
        self.matriz.append(self.lista_parado)

        self.index_lista = 0
        self.image = self.matriz[self.indice_matriz][self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        #andando pra direita
        self.lista_direita = []
        for i in range(8):
            img = caminhar_direita.subsurface((i*128,0), (128,128))
            self.lista_direita.append(img)
        self.matriz.append(self.lista_direita)

        #andando para a esquerda
        self.lista_esquerda = []
        for i in range(8):
            img = caminhar_esquerda.subsurface((i*128,0), (128,128))
            self.lista_esquerda.append(img)
        self.matriz.append(self.lista_esquerda)
        
        #socando o chão
        self.lista_atacando = []
        for i in range(30):
            img = atacando.subsurface((i*128,0), (128,128))
            self.lista_atacando.append(img)
        self.matriz.append(self.lista_atacando)

        #sumindo
        self.lista_sumindo = []
        for i in range(37):
            img = sumindo.subsurface((i*128,0), (128,128))
            self.lista_sumindo.append(img)
        self.matriz.append(self.lista_sumindo)

    def define_x(self):
        self.x = 860
        self.posicao_soco = 860

    def update(self):
        self.pressionada = pygame.key.get_pressed()
        self.letra = 26
        self.muda_tela = False
        if self.pressionada[pygame.K_RIGHT]:
            self.indice_matriz = 1
            if self.index_lista > 7:
                self.index_lista = 0
            self.index_lista += 0.5
            self.image = self.lista_direita[int(self.index_lista)]
            if self.x < 895:
                self.x += 3
        
        elif self.pressionada[pygame.K_LEFT]:
            self.indice_matriz = 2
            if self.index_lista > 7:
                self.index_lista = 0
            self.index_lista += 0.5
            self.image = self.lista_esquerda[int(self.index_lista)]
            if self.x > 5:
                self.x -= 3

        elif self.pressionada[pygame.K_SPACE]:
            self.indice_matriz = 3
            self.posicao_soco = -1
            if self.index_lista > 29:
                self.index_lista = 0
            if self.index_lista > 20:
                self.posicao_soco = self.x
            self.index_lista += 0.5
            self.image = self.lista_atacando[int(self.index_lista)]

        elif self.pressionada[pygame.K_DOWN] and self.x > 832:
            self.indice_matriz = 4
            if self.index_lista > 37:
                self.index_lista = 0
            if self.index_lista > 34:
                self.muda_tela = True
                self.index_lista = 0
            self.index_lista += 0.25
            self.image = self.lista_sumindo[int(self.index_lista)]

        else:
            self.indice_matriz = 0
            if self.index_lista > 17:
                self.index_lista = 0
            self.index_lista += 0.5
            self.image = self.lista_parado[int(self.index_lista)]
            
        self.rect.center = (self.x, self.y)

    def verifica_letra(self):
        if self.posicao_soco >= 0 and self.posicao_soco <= 32:
            self.letra = 0
        elif self.posicao_soco > 32 and self.posicao_soco <= 64:
            self.letra = 1
        elif self.posicao_soco > 64 and self.posicao_soco <= 96:
            self.letra = 2
        elif self.posicao_soco > 96 and self.posicao_soco <= 128:
            self.letra = 3
        elif self.posicao_soco > 128 and self.posicao_soco <= 160:
            self.letra = 4
        elif self.posicao_soco > 160 and self.posicao_soco <= 192:
            self.letra = 5
        elif self.posicao_soco > 192 and self.posicao_soco <= 224:
            self.letra = 6
        elif self.posicao_soco > 224 and self.posicao_soco <= 256:
            self.letra = 7
        elif self.posicao_soco > 256 and self.posicao_soco <= 288:
            self.letra = 8
        elif self.posicao_soco > 288 and self.posicao_soco <= 320:
            self.letra = 9
        elif self.posicao_soco > 320 and self.posicao_soco <= 352:
            self.letra = 10
        elif self.posicao_soco > 352 and self.posicao_soco <= 384:
            self.letra = 11
        elif self.posicao_soco > 384 and self.posicao_soco <= 416:
            self.letra = 12
        elif self.posicao_soco > 416 and self.posicao_soco <= 448:
            self.letra = 13
        elif self.posicao_soco > 448 and self.posicao_soco <= 480:
            self.letra = 14
        elif self.posicao_soco > 480 and self.posicao_soco <= 512:
            self.letra = 15
        elif self.posicao_soco > 512 and self.posicao_soco <= 544:
            self.letra = 16
        elif self.posicao_soco > 544 and self.posicao_soco <= 576:
            self.letra = 17
        elif self.posicao_soco > 576 and self.posicao_soco <= 608:
            self.letra = 18
        elif self.posicao_soco > 608 and self.posicao_soco <= 640:
            self.letra = 19
        elif self.posicao_soco > 640 and self.posicao_soco <= 672:
            self.letra = 20
        elif self.posicao_soco > 672 and self.posicao_soco <= 704:
            self.letra = 21
        elif self.posicao_soco > 704 and self.posicao_soco <= 736:
            self.letra = 22
        elif self.posicao_soco > 736 and self.posicao_soco <= 768:
            self.letra = 23
        elif self.posicao_soco > 768 and self.posicao_soco <= 800:
            self.letra = 24
        elif self.posicao_soco > 800 and self.posicao_soco <= 832:
            self.letra = 25
        elif self.posicao_soco > 832:
            self.letra = 26
        return self.letra

    def muda(self): 
        return self.muda_tela
