import pygame

pygame.init()

# SCREEN --------------------------------------------------------------------------------

WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# FPS -----------------------------------------------------------------------------------

frames = 60
clock = pygame.time.Clock()

# COLORS --------------------------------------------------------------------------------

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,215,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

# FONT ----------------------------------------------------------------------------------

text_font = pygame.font.Font("C:/Users/belaz/OneDrive/Informatique/Personnal/python/kvn-pokemon-gen-1.ttf",28)

# MENU BUTTONS --------------------------------------------------------------------------

# TEXT ------------------------------------------------

play = text_font.render("Play",True,BLUE,BLACK)
new = text_font.render("New Game",True,BLUE,BLACK)
alt_f4 = text_font.render("QUIT",True,BLUE,BLACK)

# POSITIONING -----------------------------------------

playB = play.get_rect(topleft=(450,300))
newB = new.get_rect(topleft=(400,420))
alt_f4B = alt_f4.get_rect(topleft=(450,550))

# RECTANGLES ------------------------------------------

playR = pygame.Rect(448,298,85,60)
newR = pygame.Rect(397,418,205,60)
alt_f4R = pygame.Rect(448,548,111,60)

# IMAGES --------------------------------------------------------------------------------

logo = pygame.image.load("Pokemon_logo.png")
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH,HEIGHT))

# GAME LOOP -----------------------------------------------------------------------------

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # DETECTION COLLISIONS ---------------------------------------------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playR.collidepoint(mouse_pos):
                print("PLAY")
                screen.fill(WHITE)
            
            if newR.collidepoint(mouse_pos):
                print("NEWBIE")
                screen.fill(BLACK)

            if alt_f4R.collidepoint(mouse_pos):
                print("LEAVE")
                running = False
    
    mouse_pos = pygame.mouse.get_pos()

    screen.blit(background,(0,0))
    screen.blit(logo,(330,50))
    
    # AFFICHAGE RECTANGLES ----------------------------------------------------------------

    pygame.draw.rect(screen,YELLOW,playR,2)
    pygame.draw.rect(screen,YELLOW,newR,2)
    pygame.draw.rect(screen,YELLOW,alt_f4R,2)

    screen.blit(play,playB)
    screen.blit(new,newB)
    screen.blit(alt_f4,alt_f4B)

    # AFFICHAGE/FPS ------------------------------------------------------------------------

    pygame.display.flip()
    clock.tick(frames)
    

pygame.quit()