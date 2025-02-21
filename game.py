import pygame
import random
import combat
import pokemon
from pylint import pyreverse

pygame.init()

# SCREEN ------------------------------------------------------------

WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# FPS ---------------------------------------------------------------

frames = 60
clock = pygame.time.Clock()

# COLORS ------------------------------------------------------------

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
DARKGREEN = (0,170,50)
BLUE = (0,0,255)
YELLOW = (255,215,0)

bold_font = pygame.font.Font("assets/fonts/kvn-97.ttf",38)
text_font = pygame.font.Font("assets/fonts/kvn-pokemon-gen-1.ttf",30)

# POKEMONS ----------------------------------------------------------------------------------------------

pokemon_list = [
    
    pokemon.Pokemon("Abra", 25, 15, 30, ["Psy"], "assets/sprites/back/0063(1).png"),
    pokemon.Pokemon("Bulbizarre", 45, 49, 49, ["Plante", "Poison"], "assets/sprites/back/0001(1).png"),
    pokemon.Pokemon("Evoli", 55, 50, 45, ["Normal"], "assets/sprites/back/0133(1).png"),
    pokemon.Pokemon("Pikachu", 35, 30, 55, ["Électrique"], "assets/sprites/back/0025(1).png"),
    pokemon.Pokemon("Salamèche", 39, 43, 52, ["Feu"], "assets/sprites/back/0004(1).png"),
    pokemon.Pokemon("Mewtwo", 106, 90, 150, ["Psy"], "assets/sprites/back/0150(1).png"),
    pokemon.Pokemon("Ectoplasma", 50, 55, 65, ["Spectre", "Poison"], "assets/sprites/back/0094(1).png"),
    pokemon.Pokemon("Chenipan", 45, 35, 29, ["Insecte"], "assets/sprites/back/0010(1).png"),
    pokemon.Pokemon("Psyduck", 50, 48, 52, ["Eau"], "assets/sprites/back/0054(1).png"),
    pokemon.Pokemon("Ronflex", 160, 65, 110, ["Normal"], "assets/sprites/back/0143(1).png"),
    pokemon.Pokemon("Papilusion", 60, 50, 45, ["Insecte", "Vol"], "assets/sprites/back/0012(1).png"),
    pokemon.Pokemon("Rondoudou", 115, 45, 50, ["Fée", "Normal"], "assets/sprites/back/0039(1).png"),
    pokemon.Pokemon("Slowbro", 95, 80, 75, ["Eau", "Psy"], "assets/sprites/back/0080(1).png"),
    pokemon.Pokemon("Moltres", 90, 90, 100, ["Feu", "Vol"], "assets/sprites/back/0146(1).png"),
    pokemon.Pokemon("Vaporeon", 130, 60, 65, ["Eau"], "assets/sprites/back/0134(1).png"),
    pokemon.Pokemon("Zapdos", 90, 85, 90, ["Électrique", "Vol"], "assets/sprites/back/0145(1).png"),
    pokemon.Pokemon("Scyther", 70, 80, 110, ["Insecte", "Vol"], "assets/sprites/back/0123(1).png"),
    pokemon.Pokemon("Dugtrio", 35, 35, 100, ["Sol"], "assets/sprites/back/0051(1).png"),
    pokemon.Pokemon("Flareon", 65, 60, 130, ["Feu"], "assets/sprites/back/0136(1).png"),
    pokemon.Pokemon("Gyarados", 95, 79, 125, ["Eau", "Vol"], "assets/sprites/back/0130(1).png"),
    pokemon.Pokemon("Dracaufeu", 78, 85, 130, ["Feu", "Vol"], "assets/sprites/back/0006(1).png"),
]

opponent_list = [
    
    pokemon.Pokemon("Abra", 25, 15, 30, ["Psy"], "assets/sprites/front/0063.png"),
    pokemon.Pokemon("Bulbizarre", 45, 49, 49, ["Plante", "Poison"], "assets/sprites/front/0001.png"),
    pokemon.Pokemon("Evoli", 55, 50, 45, ["Normal"], "assets/sprites/front/0133.png"),
    pokemon.Pokemon("Pikachu", 35, 30, 55, ["Électrique"], "assets/sprites/front/0025.png"),
    pokemon.Pokemon("Salamèche", 39, 43, 52, ["Feu"], "assets/sprites/front/0004.png"),
    pokemon.Pokemon("Mewtwo", 106, 90, 150, ["Psy"], "assets/sprites/front/0150.png"),
    pokemon.Pokemon("Ectoplasma", 50, 55, 65, ["Spectre", "Poison"], "assets/sprites/front/0094.png"),
    pokemon.Pokemon("Chenipan", 45, 35, 29, ["Insecte"], "assets/sprites/front/0010.png"),
    pokemon.Pokemon("Psyduck", 50, 48, 52, ["Eau"], "assets/sprites/front/0054.png"),
    pokemon.Pokemon("Ronflex", 160, 65, 110, ["Normal"], "assets/sprites/front/0143.png"),
    pokemon.Pokemon("Papilusion", 60, 50, 45, ["Insecte", "Vol"], "assets/sprites/front/0012.png"),
    pokemon.Pokemon("Rondoudou", 115, 45, 50, ["Fée", "Normal"], "assets/sprites/front/0039.png"),
    pokemon.Pokemon("Slowbro", 95, 80, 75, ["Eau", "Psy"], "assets/sprites/front/0080.png"),
    pokemon.Pokemon("Moltres", 90, 90, 100, ["Feu", "Vol"], "assets/sprites/front/0146.png"),
    pokemon.Pokemon("Vaporeon", 130, 60, 65, ["Eau"], "assets/sprites/front/0134.png"),
    pokemon.Pokemon("Zapdos", 90, 85, 90, ["Électrique", "Vol"], "assets/sprites/front/0145.png"),
    pokemon.Pokemon("Scyther", 70, 80, 110, ["Insecte", "Vol"], "assets/sprites/front/0123.png"),
    pokemon.Pokemon("Dugtrio", 35, 35, 100, ["Sol"], "assets/sprites/front/0051.png"),
    pokemon.Pokemon("Flareon", 65, 60, 130, ["Feu"], "assets/sprites/front/0136.png"),
    pokemon.Pokemon("Gyarados", 95, 79, 125, ["Eau", "Vol"], "assets/sprites/front/0130.png"),
    pokemon.Pokemon("Dracaufeu", 78, 85, 130, ["Feu", "Vol"], "assets/sprites/front/0006.png"),
]

player = random.choice(pokemon_list)
opponent = random.choice(opponent_list)
playerI = pygame.image.load(player.image_path)
playerI = pygame.transform.scale(playerI,(300,300))
opponentI = pygame.image.load(opponent.image_path)
opponentI = pygame.transform.scale(opponentI,(300,300))

fight = combat.Fight(player,opponent)

# IMAGES -----------------------------------------------------------

arena = pygame.image.load("assets/images/arene.png")
arena = pygame.transform.scale(arena,(WIDTH,HEIGHT))

# TEXT (EVERYTHING) ------------------------------------------------

    #TEXT ---------------------------------------------

player = bold_font.render(fight.player.nom.upper(),True,BLACK) 
opponent = bold_font.render(fight.opponent.nom.upper(),True,BLACK)
life = bold_font.render(str(fight.plife),True,BLACK) 
lifed = bold_font.render(str(fight.lifedefaultP),True,BLACK)
win = text_font.render("You won!",True,BLACK)
                
x = text_font.render(f"{fight.player.nom}",True,BLACK)
y = text_font.render(f"{fight.opponent.nom}",True,BLACK)
isattacking = text_font.render("is attacking...",True,BLACK)
ishealing = text_font.render("is healing...",True,BLACK)
winR = win.get_rect(topleft=(140,650))

ask = text_font.render("What do you use?",True,BLACK)
heal = text_font.render("Heal",True,BLACK)

    #RECTANGLES ---------------------------------------
playerR = player.get_rect(topleft=(610,430))
opponentR = opponent.get_rect(topleft=(100,50))
lifeR = life.get_rect(topleft=(625,520))
lifedR = lifed.get_rect(topleft=(790,520)) 
xR = x.get_rect(topleft=(50,600))
yr = y.get_rect(topleft=(50,600))
isattackingR = isattacking.get_rect(topleft=(50,650))
ishealingR = ishealing.get_rect(topleft=(50,650))
askR = ask.get_rect(topleft=(60,600))
healR = heal.get_rect(topleft=(60,650))

# BUTTONS ---------------------------------------------------------

lifeBAR = pygame.Rect(660,498,250,6)
lifeBAR2 = pygame.Rect(168,122,250,6)

fightB = pygame.Rect(537,630,210,45)
pkmnB = pygame.Rect(785,629,92,52)
itemB = pygame.Rect(535,700,165,45)
runB = pygame.Rect(789,700,130,45)
healB = pygame.Rect(50,650,100,45)

# FUNCTIONS -------------------------------------------------------

barPLAYER = 250
barOPPONENT = 250

def display():

    screen.blit(arena,(0,0))
    screen.blit(playerI,(100,282))
    screen.blit(opponentI,(600,60))
    
    pygame.draw.rect(screen,RED,lifeBAR)
    pygame.draw.rect(screen,RED,lifeBAR2)
    lifeBPOKEMON = pygame.Rect(660,498,barPLAYER,6)
    lifeBOPPONENT = pygame.Rect(168,122,barOPPONENT,6)
    
    pygame.draw.rect(screen,RED,fightB,2)
    pygame.draw.rect(screen,GREEN,pkmnB,2)
    pygame.draw.rect(screen,YELLOW,itemB,2)
    pygame.draw.rect(screen,BLUE,runB,2)
    pygame.draw.rect(screen,DARKGREEN,lifeBPOKEMON)
    pygame.draw.rect(screen,DARKGREEN,lifeBOPPONENT)
    screen.blit(player,playerR)
    screen.blit(opponent,opponentR)

    screen.blit(life,lifeR)
    screen.blit(lifed,lifedR) 

def barstatus():
    global barPLAYER
    global barOPPONENT
    deltaP = fight.plife/fight.lifedefaultP
    print(deltaP)
    deltaO = fight.olife/fight.lifedefaultO
    print(deltaO)
    barPLAYER *= deltaP
    barOPPONENT *= deltaO
    

#GAME LOOP --------------------------------------------------------

running = True
while running:

    mouse_pos = pygame.mouse.get_pos()
    display()
    def check_win():
            if fight.olife <= 0:
                    screen.fill(WHITE)
                    display()
                    pygame.time.delay(500)
                    screen.blit(win,winR)
                    pygame.display.flip()
                    return True
    def check_lost():
        if fight.plife <= 0:
                lose = text_font.render("You lost...",True,BLACK)
                loseR = lose.get_rect(topleft=(140,650))
                screen.fill(WHITE)
                display()
                pygame.time.delay(500)
                screen.blit(lose,loseR)
                pygame.display.flip()
                return True

    check_win()
    check_lost()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #CHECK WIN ------------------------------------------------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            #FIGHT BUTTON ------------------------------------------------------------------
            
            if fightB.collidepoint(mouse_pos):        
                affichage = True
                while affichage != False:
                    screen.blit(x,xR)
                    screen.blit(isattacking,isattackingR)
                    pygame.display.flip()
                    fight.attack_player()
                    barstatus()
                    if fight.olife <= 0:
                         affichage = False
                    
                    pygame.time.delay(1000)
                    
                    if check_win() == True:
                         affichage = False

                    screen.fill(WHITE)
                    display()
                    
                    pygame.time.delay(1000)
                    screen.blit(y,yr)
                    screen.blit(isattacking,isattackingR)
                    pygame.display.flip()
                    fight.attack_opponent()
                    barstatus()
                    if fight.plife <= 0:
                        affichage = False
                    
                    if check_lost() == True:
                         affichage = False
                    
                    affichage = False
                    
            
            #ITEM BUTTON -------------------------------------------------------------------        

            if itemB.collidepoint(mouse_pos):
                screen.blit(x,xR)
                screen.blit(ishealing,ishealingR)
                pygame.display.flip()
                fight.heal()
                pygame.time.delay(1000)
                
                screen.fill(WHITE)
                display()
                pygame.time.delay(500)
                screen.blit(y,yr)
                screen.blit(isattacking,isattackingR)
                pygame.display.flip()
                pygame.time.delay(1000)
                life = bold_font.render(str(fight.plife),True,BLACK) 
                fight.attack_opponent()
                #affichage = False
                
            """PYREVERSE STP FAIS UN DIAGRAMME DE CLASSE"""


            #RUN BUTTON --------------------------------------------------------------------
            
            if runB.collidepoint(mouse_pos):
                affichage = False
                running = False

    check_win()
    check_lost()

    life = bold_font.render(str(fight.plife),True,BLACK) 
    display()
    
    pygame.display.flip()

pygame.quit()