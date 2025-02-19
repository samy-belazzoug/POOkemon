import tkinter as tk
from PIL import Image, ImageTk
import pygame

class Pokemon:
    def __init__(self, nom, points_de_vie, defense, attaque, types, image_path):
        
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.defense = defense
        self.attaque = attaque
        self.types = types 
        self.image_path = image_path
        
        
        self.image = self.load_image(image_path)

    def load_image(self, image_path):
        
        try:
            image = Image.open(image_path)
            image = image.resize((100, 100))  
            return ImageTk.PhotoImage(image)
        except FileNotFoundError:
            print(f"Erreur : L'image pour {self.nom} n'a pas été trouvée.")
            return None
    
    def afficher(self, parent):
        """affiche le pokémon dans une interface graphique."""
        label_image = tk.Label(parent, image=self.image)
        label_image.pack()

    def afficher_caracteristiques(self):
        """caractéristiques du Pokémon."""
        print(f"Nom: {self.nom}")
        print(f"Type(s): {', '.join(self.types)}")
        print(f"Points de vie: {self.points_de_vie}")
        print(f"Défense: {self.defense}")
        print(f"Attaque: {self.attaque}")


pokemon_list = [
    Pokemon("Abra", 25, 15, 30, ["Psy"], "assets/pictures/abra.png"),
    Pokemon("Bulbizarre", 45, 49, 49, ["Plante", "Poison"], "assets/pictures/bulbizarre.png"),
    Pokemon("Chenipan", 45, 35, 29, ["Insecte"], "assets/pictures/chenipan.png"),
    Pokemon("Chikorita", 45, 55, 49, ["Plante"], "assets/pictures/chikorita.png"),
    Pokemon("Darkrai", 100, 65, 90, ["Ténèbres"], "assets/pictures/darkrai.png"),
    Pokemon("Dugtrio", 35, 35, 100, ["Sol"], "assets/pictures/dugtrio.png"),
    Pokemon("Ectoplasma", 50, 55, 65, ["Spectre", "Poison"], "assets/pictures/ectoplasma.png"),
    Pokemon("Evoli", 55, 50, 45, ["Normal"], "assets/pictures/evoli.png"),
    Pokemon("Flareon", 65, 60, 130, ["Feu"], "assets/pictures/flareon.png"),
    Pokemon("Groudon", 100, 90, 150, ["Sol"], "assets/pictures/groudon.png"),
    Pokemon("Gyarados", 95, 79, 125, ["Eau", "Vol"], "assets/pictures/gyarados.png"),
    Pokemon("Mega-Dracaufeu", 78, 85, 130, ["Feu", "Vol"], "assets/pictures/mega_dracaufeu.png"),
    Pokemon("Mewtwo", 106, 90, 150, ["Psy"], "assets/pictures/mewtwo.png"),
    Pokemon("Moltres", 90, 90, 100, ["Feu", "Vol"], "assets/pictures/moltres.png"),
    Pokemon("Papilusion", 60, 50, 45, ["Insecte", "Vol"], "assets/pictures/papilusion.png"),
    Pokemon("Pikachu", 35, 30, 55, ["Électrique"], "assets/pictures/pikachu.png"),
    Pokemon("Psyduck", 50, 48, 52, ["Eau"], "assets/pictures/psyduck.png"),
    Pokemon("Rondoudou", 115, 45, 50, ["Fée", "Normal"], "assets/pictures/rondoudou.png"),
    Pokemon("Ronflex", 160, 65, 110, ["Normal"], "assets/pictures/ronflex.png"),
    Pokemon("Salamèche", 39, 43, 52, ["Feu"], "assets/pictures/salameche.png"),
    Pokemon("Scyther", 70, 80, 110, ["Insecte", "Vol"], "assets/pictures/scyther.png"),
    Pokemon("Slowbro", 95, 80, 75, ["Eau", "Psy"], "assets/pictures/slowbro.png"),
    Pokemon("Solgaleo", 137, 107, 137, ["Acier", "Psy"], "assets/pictures/solgaleo.png"),
    Pokemon("Umbreon", 95, 110, 60, ["Ténèbres"], "assets/pictures/umbreon.png"),
    Pokemon("Vaporeon", 130, 60, 65, ["Eau"], "assets/pictures/vaporeon.png"),
    Pokemon("Zapdos", 90, 85, 90, ["Électrique", "Vol"], "assets/pictures/zapdos.png")
]


for pokemon in pokemon_list:
    pokemon.afficher_caracteristiques()


root = tk.Tk()
root.title("Pokémon")


for pokemon in pokemon_list:
    pokemon.afficher(root)

root.mainloop()
