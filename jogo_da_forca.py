from funçoes import*
import pygame
from pygame.locals import*
from sys import exit




#variaveis
arquivo_palavras = 'palavras_secretas.txt'
chances = 7
tentativas = 0
tentativas_de_letra = [' ', '-']
palavra_camuflada = ''
letra = ' '
ganhou = False

palavra_secreta ,dica = palavra_aleatoria(arquivo_palavras)


#Cores

branco = (255, 255, 255)
preto = (0, 0, 0)



#Configuração da janela

largura_janela = 1000
altura_janela = 600
cor_de_fundo = branco

#Fontes
fonte = pygame.font.SysFont("Courier New", 50)
fonte_rb = pygame.font.SysFont("Courier New", 30)
fonte_pequena = pygame.font.SysFont("Courier New", 20)




#inicia pygame
pygame.init()
pygame.font.init()

#inicia a janela
janela = pygame.display.set_mode((largura_janela ,altura_janela))
pygame.display.set_caption('Jogo da Forca')
relogio = pygame.time.Clock()

while True:
    #relogio.tick(20)
    janela.fill(cor_de_fundo)
    menssagem = f'Você tem {chances} chances'
    desenhar_forca(janela)



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
        if event.type == pygame.KEYDOWN:
            letra = str(pygame.key.name(event.key)).upper()
            

    
    #Jogo
    palavra_camuflada = camuflar_palavra(palavra_secreta,palavra_camuflada, tentativas_de_letra)
    #print(palavra_secreta, palavra_camuflada)
    tentativas_de_letra, tentativas = tentativa_uma_letra(tentativas_de_letra, palavra_secreta, letra, tentativas)
    #print(tentativas_de_letra, tentativas,palavra_secreta)
    palavra_jogo(janela, fonte, palavra_camuflada, (200,500))
    palavra_jogo(janela,fonte_pequena, f"Dica:{dica}", (700,50))
    if tentativas >= 1:
        desenhar_cabeça(janela)
    if tentativas >= 2:
        desenhar_tronco(janela)
    if tentativas >= 3:
        desenhar_bracod(janela)
    if tentativas >= 4:
        desenhar_bracoe(janela)
    if tentativas >= 5:
        desenhar_pernad(janela)
    if tentativas >= 6:
        desenhar_pernae(janela)
    if tentativas >= 7:
        janela.fill(branco)
        palavra_jogo(janela, fonte, f"Voce perdeu, a palavra secreta é:{palavra_secreta}")    
    ganhou = Restart_do_Jogo(palavra_camuflada,tentativas, letra, tentativas_de_letra)
    if ganhou:
        janela.fill(branco)
        palavra_jogo(janela, fonte, "Parabens!!!Você ganhor :)", (100, 300))
    
    pygame.display.flip()

