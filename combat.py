import pygame
import random

class Fight:
    def __init__(self,player,plife,olife,opponent:list=[],tour:int=0): 
        self.player = player
        self.opponent = random.choice(opponent)
        self.tour = tour
        self.plife = plife
        self.olife = olife

    def attack(self,points): #attaquer
        if self.tour == 0: #player attaque
            
            dodge = random.randint(0,10)
            if dodge not in [0,1,3,5,6,7,8,10]: #Si dodge == 2,4,9
                self.tour = 1
                return print("Dodged !\n")
            
            else:
                print(f"{self.player} attacked !")
                self.olife -= points
                pygame.time.delay(1000)
                print(f"{self.opponent} lost {points} points. Hes got {self.olife} left.\n")
                pygame.time.delay(1000)  
                self.tour = 1
                return f"Au tour de {self.opponent}"
        
        pygame.time.delay(1000)
        if self.tour == 1: #player attaque
            
            dodge_detect = random.randint(0,10)
            if dodge_detect not in [0,1,3,5,6,7,8,10]: #Si dodge == 2,4,9
                self.tour = 0
                return print("Dodged !\n")
            
            else:
                print(f"{self.opponent} attacked !")
                self.plife -= points
                pygame.time.delay(1000)
                print(f"{self.player} lost {points} points. Hes got {self.plife} left.\n")
                self.tour = 0
                pygame.time.delay(1000)
                return f"Its time for {self.player}"

    def defend(self): #defendre
        pass

    def heal(self,points): #soigner
        if self.tour == 0: #player attaque
            print(f"{self.player} healed")
            self.olife += points
            pygame.time.delay(1000)
            print(f"Hes got {self.plife} points left\n")
            self.tour = 1
            pygame.time.delay(1000)
            return f"Its time for {self.opponent}"
        
        pygame.time.delay(500)
        if self.tour == 1: #player attaque
            print(f"{self.opponent} attacked !")
            self.plife += points
            pygame.time.delay(1000)
            print(f"Hes got {self.plife} points left\n")
            self.tour = 0
            pygame.time.delay(1000)
            return f"Its time for {self.player}"
    
    def fight(self):
        while self.plife > 0 or self.olife > 0:
            i = int(input(f"What's your plans (You have {self.plife} left) ?\n1: Attack\n2: Heal\n"))
            if i == 1:
                pygame.time.delay(1000)
                self.attack(random.randint(4,12))
                if self.olife <= 0:
                    print (f"{self.player} wins!")
                    break

            if i == 2:
                pygame.time.delay(1000)
                self.heal(5)            

            if self.olife < 7:
                p = random.randint(0,2)
                if p == 0:
                    pygame.time.delay(1000)
                    self.heal(5)
                    pygame.time.delay(1000)
                else:
                    pygame.time.delay(1000)
                    self.attack(random.randint(4,12))
                    pygame.time.delay(1000)
            else:
                self.attack(random.randint(4,12))
            
            if self.plife <= 0:
                print (f"{self.player} wins!")
                break

            
combat = Fight("Pikachu",20,20,["Salameche","Bulbizzare","Carapuce","Evoli"])
combat.fight()