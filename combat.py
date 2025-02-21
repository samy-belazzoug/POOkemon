import pygame
import random
import pokemon

class Fight:
    def __init__(self,player:pokemon.Pokemon,opponent:pokemon.Pokemon,tour:int=0): 
        self.player = player
        self.opponent = opponent
        self.tour = tour
        self.plife = player.points_de_vie
        self.olife = opponent.points_de_vie
        self.lifedefaultP = self.plife
        self.lifedefaultO = self.olife

    def get_lifeP(self):
        return self.lifedefaultP

    def get_lifeO(self):
        return self.lifedefaultO
    

    def attack_player(self): #attaquer
        points = random.randint(int(self.player.attaque/1.5),int(self.player.attaque))
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
                return print(f"Au tour de {self.opponent}")
        
    def attack_opponent(self): #attaquer
        points = random.randint(int(self.opponent.attaque/1.5),int(self.opponent.attaque))
        if self.tour == 1: #opponent attaque
            
            dodge = random.randint(0,10)
            if dodge not in [0,1,3,5,6,7,8,10]: #Si dodge == 2,4,9
                self.tour = 0
                return print("Dodged !\n")
             
            if self.olife <= 7:
                p = random.randint(0,2)
                if p == 0:
                    pygame.time.delay(1000)
                    self.heal()
            else:
                print(f"{self.opponent} attacked !")
                self.plife -= points
                pygame.time.delay(1000)
                print(f"{self.player} lost {points} points. Hes got {self.plife} left.\n")
                pygame.time.delay(1000)  
                self.tour = 0
                return print(f"Au tour de {self.player}")
        

    def defend(self): #defendre
        pass

    def heal(self): #soigner
        if self.tour == 0: #player attaque
            print(f"{self.player} healed")
            if self.plife >= 16:
                self.plife = self.lifedefaultP
            else:
                self.plife += 5
                pygame.time.delay(1000)
                print(f"Hes got {self.plife} points left\n")
                self.tour = 1
                pygame.time.delay(1000)
                return f"Its time for {self.opponent}"
        
        pygame.time.delay(500)
        if self.tour == 1: #player attaque
            print(f"{self.opponent} healed !")
            if self.plife >= 16:
                self.plife = self.lifedefaultP
            else:
                self.olife += 5
                pygame.time.delay(1000)
                print(f"Hes got {self.olife} points left\n")
                self.tour = 0
                pygame.time.delay(1000)
                return f"Its time for {self.player}"


    def fight(self):
        """EXECUTE A FIGHT IN THE TERMINAL"""
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
                self.heal()            

            if self.olife < 7:
                p = random.randint(0,2)
                if p == 0:
                    pygame.time.delay(1000)
                    self.heal()
                    pygame.time.delay(1000)
                else:
                    pygame.time.delay(1000)
                    self.attack(random.randint(self.player.attaque/2,self.player.attaque))
                    pygame.time.delay(1000)
            else:
                self.attack(random.randint(4,12))
            
            if self.plife <= 0:
                print (f"{self.opponent} wins!")
                break


if __name__ == "__main__":   
    combat = Fight("Pikachu",20,20,["Salameche","Bulbizzare","Carapuce","Evoli",])
    #combat.fight()