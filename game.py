from random import randint

class Person:
    def __init__(self, name: str, hp: int, mp: int, atk: int):
        self.name = name 
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.atk_high = atk + 10
        self.atk_low  = atk - 10
        self.actions = ["Attack", "Magic"] # Hardcoded for now

    def get_stat(self):
        print(f"Player: {self.name}, Health:{self.hp}/{self.max_hp}, Magic:{self.mp}/{self.max_mp}")

    def generate_dmg(self):
        return randint(self.atk_low, self.atk_high + 1)

    def take_dmg(self, dmg: int):
        self.hp = 0 if self.hp < dmg else self.hp - dmg
        return self.hp
    
    def choose_action(self):
        i = 1
        for action in self.actions:
            print(f"{i}. {action}\n")
            i+=1
