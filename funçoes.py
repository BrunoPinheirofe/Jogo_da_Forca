import random
import pygame
from pygame.locals import*

#iniciar pygame
pygame.init()

#Cores
branco = (255, 255, 255)
preto = (0, 0, 0)


def palavra_aleatoria(nome_arquivo): #fução que pega uma palavra aleatoraia e sua categoria do aquivo txt
    with open(nome_arquivo, "rt") as arquivo:
        linhas = arquivo.readlines()
        linha_aleatoria = random.choice(linhas).strip()
        palavra, dica = linha_aleatoria.split(';')
        return palavra.upper(), dica.upper()


#desenhos

def desenhar_forca(janela):
    pygame.draw.rect(janela, branco, (0, 0, 1000, 600))
    pygame.draw.line(janela, preto, (100, 500), (100, 100), 10)
    pygame.draw.line(janela, preto, (50, 500), (150, 500), 10)
    pygame.draw.line(janela, preto, (100, 100), (300, 100), 10)
    pygame.draw.line(janela, preto, (300, 100), (300, 150), 10)

def desenhar_cabeça(janela):
    pygame.draw.circle(janela, preto, (300,200), 50, 10)
def desenhar_tronco(janela):
    pygame.draw.line(janela, preto, (300, 250), (300, 350), 10)
def desenhar_bracod(janela):
    pygame.draw.line(janela, preto, (300,260), (375, 350), 10)
def desenhar_bracoe(janela):
    pygame.draw.line(janela, preto, (300, 260), (255, 350), 10)
def desenhar_pernad(janela):
    pygame.draw.line(janela, preto, (300, 350), (375, 450), 10)
def desenhar_pernae(janela):
    pygame.draw.line(janela,preto,(300, 350), (255, 450), 10)
    

def reset_button(janela, fonte):
    pygame.draw.rect(janela, preto, (700, 100, 200, 65))
    texto = fonte.render('Reset', 1, branco)
    janela.blit(texto, (740, 120))

def camuflar_palavra(palavra_secreta, palavra_camuflada, tentativas_de_letras):
    palavra_camuflada = palavra_secreta
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n:n + 1] not in tentativas_de_letras:
            palavra_camuflada = palavra_camuflada.replace(palavra_camuflada[n], '-')
    return palavra_camuflada

def tentativa_uma_letra(tentativas_de_letras, palavra_secreta, letra, tentativas):
    if letra not in tentativas_de_letras:
        tentativas_de_letras.append(letra)
        if letra not in palavra_secreta:
            tentativas += 1
    elif letra in tentativas_de_letras:
        pass
    return tentativas_de_letras, tentativas

def palavra_jogo(janela, fonte, palavra_camuflada, cord :tuple):
    palavra = fonte.render(palavra_camuflada, 1, preto)
    janela.blit(palavra, cord)

def Restart_do_Jogo(palavra_camuflada, chance, letra, tentativas_de_letras):
    count = 0
    limite = len(palavra_camuflada)
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n] != '-':
            count += 1
    if count == limite:
        print('Ok')
        return True
