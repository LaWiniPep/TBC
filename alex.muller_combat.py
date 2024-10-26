import alexMuller_tcb


def main():
    hero = alexMuller_tcb.Character("Hero", 10, 50, 5, 2)
  
    monster = alexMuller_tcb.Character("Monster", 20, 30, 5, 0)
  
  
    hero.printStats()
    monster.printStats()

    hero.fight(hero, monster)

if __name__ == "__main__":
    main()
