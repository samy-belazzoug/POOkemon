import pygame
import combat

pygame.init()
fight = combat.Fight(["Pikachu","Salameche","Bulbizzare","Nidorina","Carapuce","Evoli",],20,20,["Salameche","Bulbizzare","Carapuce","Evoli",])

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
BLUE = (0,0,255)
YELLOW = (255,215,0)

bold_font = pygame.font.Font("assets/fonts/kvn-97.ttf",38)
text_font = pygame.font.Font("assets/fonts/kvn-pokemon-gen-1.ttf",30)

# IMAGES -----------------------------------------------------------

arena = pygame.image.load("assets/images/arene.png")
arena = pygame.transform.scale(arena,(WIDTH,HEIGHT))

# TEXT (EVERYTHING) ------------------------------------------------

    #TEXT ---------------------------------------------
player = bold_font.render(fight.player.upper(),True,BLACK) 
opponent = bold_font.render(fight.opponent.upper(),True,BLACK)
life = bold_font.render(str(fight.plife),True,BLACK) 
lifed = bold_font.render(str(fight.lifedefaultP),True,BLACK)
win = text_font.render("You won!",True,BLACK)
                

x = text_font.render(f"{fight.player}",True,BLACK)
y = text_font.render(f"{fight.opponent}",True,BLACK)
isattacking = text_font.render("is attacking...",True,BLACK)
winR = win.get_rect(topleft=(140,650))

    #RECTANGLES ---------------------------------------
playerR = player.get_rect(topleft=(610,430))
opponentR = opponent.get_rect(topleft=(100,50))
lifeR = life.get_rect(topleft=(660,520))
lifedR = lifed.get_rect(topleft=(790,520)) 
xR = x.get_rect(topleft=(50,600))
yr = y.get_rect(topleft=(50,600))
isattackingR = isattacking.get_rect(topleft=(50,650))

# BUTTONS ---------------------------------------------------------

fightB = pygame.Rect(537,630,210,45)
pkmnB = pygame.Rect(785,629,92,52)
itemB = pygame.Rect(535,700,165,45)
runB = pygame.Rect(789,700,130,45)

# FUNCTIONS -------------------------------------------------------

def display():
    screen.blit(arena,(0,0))
    pygame.draw.rect(screen,RED,fightB,2)
    pygame.draw.rect(screen,GREEN,pkmnB,2)
    pygame.draw.rect(screen,YELLOW,itemB,2)
    pygame.draw.rect(screen,BLUE,runB,2)

    screen.blit(player,playerR)
    screen.blit(opponent,opponentR)

    screen.blit(life,lifeR)
    screen.blit(lifed,lifedR) 
  


#GAME LOOP --------------------------------------------------------
running = True
while running:

    mouse_pos = pygame.mouse.get_pos()
    life = bold_font.render(str(fight.plife),True,BLACK) 

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
                    if fight.plife <= 0:
                        affichage = False
                    
                    if check_lost() == True:
                         affichage = False
                    
                         
                    affichage = False

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