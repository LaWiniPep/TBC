"""
Turn based game where you fight a monster
Character stats printed and then the stats change game play
Once one characters HP is 0 other character wins
"""

import random

def main():
    self = Character()
    self.printStats()

class Character(object):
    def __init__(self, name = "anonymous", hitPoint = 10, hitChance = 50, maxDamage = 5, armor = 2):
        super().__init__()
        self.__name = name
        self.__hitPoint = hitPoint
        self.__maxDamage = maxDamage
        self.__hitChance = hitChance
        self.__armor = armor
#Name        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
#Hit Points  
    @property
    def hitPoint(self):
        return self.__hitPoint
    
    @hitPoint.setter
    def hitPoint(self, value):
        self.__hitPoint = value      
#Max Damage    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        self.__maxDamage = value
#Hit Chance           
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        self.__hitChance = value
#Armor          
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        self.__armor = value
#Print Stats    
    def printStats(self):
        print(f"""
       {self.__name}
==================

Hit Points: {self.__hitPoint}
Hit Chance: {self.__hitChance}
Max Damage: {self.__maxDamage}
Armor:      {self.__armor}
""")

    
#Attack    
    def attack(self):
        if random.randint(0, 100) <= self.__hitChance:
            hit = random.randint(1, self.__maxDamage)
           
            return hit                 
        else:
            print(f"{self.name} Misses!")
            return 0


#Fight
    def fight(self, hero, monster):
        keepGoing = True
        while keepGoing:
            heroHit = hero.attack()
            if heroHit:
                hitDamage = heroHit - monster.armor
                if hitDamage < 0:
                    hitDamage = 0
                monster.hitPoint -= hitDamage
                if monster.hitPoint <= 0:
                    print("Hero wins!")
                    keepGoing = False
                else:
                    print(f"{hero.name} hits monster for {hitDamage} after Monster absorbed {monster.armor} with their armor. Monster now has {monster.hitPoint} HP")

            if keepGoing:
                monsterHit = monster.attack()
                if monsterHit:
                    hitDamage = monsterHit - hero.armor
                    if hitDamage < 0:
                        hitDamage = 0
                    hero.hitPoint -= hitDamage
                    if hero.hitPoint <= 0:
                        print("Monster wins!")
                        keepGoing = False
                    else:
                        print(f"{monster.name} hits hero for {hitDamage} after Hero absorbed {hero.armor} with their armor. Hero now has {hero.hitPoint} HP")
            if keepGoing:
                input("Press enter to continue to the next round....")