import random as r
import os, sys
from time import sleep

def printer(sentence): #Denna funktion gör att texten skrivs ut i terminalen tecken för tecken.
    for character in sentence:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.005)

def clear(): #Denna funktion clearar terminalen 👍
    os.system('cls' if os.name == 'nt' else 'clear')

def open_door(potion_counter, has_potion): #Funktion för att öppna en dörr :)
    while True:
        printer("Choose a door: 1, 2, 3\n")
        door_choice = input()
        clear()
        if door_choice in ["1","2","3"]:
            sleep(1)
            if potion_counter != 0:
                potion_counter -= 1
            if potion_counter == 0 and has_potion == True:
                has_potion = False
                player.STR -= 2
            door_action = r.choice(door_alt)
            if door_action == "trap": #trap
                player.update_HP()
                printer(f"You encountered a trap, you lost 1 health. Your health is now {player.HP}.")
                input()
                break
            elif door_action == "monster": #monster
                monster.monster_fight()
                if monster.STR >= player.STR:
                    player.update_HP()
                    printer(f"You encountered a monster and lost the fight, you lost 1 health. Your health is now {player.HP}.")
                    input()
                    break
                else:
                    player.level_up()
                    printer(f"You encountered a monster and won the fight, you gained 1 level. Your level is now {player.LVL}.")
                    input()
                    monster.dif_up()
                    break
            else: #Chest
                if r.randint(1,2) == 2:
                    if r.randint(1,2) == 1 and potion_counter == 0:
                        player.HP += 1
                        printer(f"You found a Potion of Healing, your health is now increased by 1. Your health is now {player.HP}.")
                        input()
                    else:
                        potion_counter = 3
                        has_potion = True
                        player.STR += 2
                        printer(f"You found a Potion of Strength, your strength is now increased by 2 for 3 doors. Your strength is now {player.STR}.")
                        input()
                elif item_list and r.randint(1,2) == 1:
                    WhichItem = r.choice(item_list)
                    item_list.remove(WhichItem)
                    player.INV.append(WhichItem)
                    monster.dif_up()
                    printer(f"You encountered a chest, you gained a {WhichItem.weapon} and with the strength {WhichItem.weaponstr}.")
                    input()
                else:
                    printer("You encountered a chest, it was empty.")
                    input()
                break
        elif door_choice == "joel":
            player.LVL = 10
        else:
            printer("Write a number 1-3 you fuckin' moron")
            print()

class Player():
    def __init__(self):
        self.STR = 5
        self.HP = 10
        self.LVL = 0
        self.INV = []
    def update_HP(self):
        self.HP -= 1
    def equip_weapon(self, amount):
        self.STR += amount
    def level_up(self):
        self.LVL += 1
    def display_stats(self):
        printer(f"""
-------Stats-------
Strength: {self.STR}
Health: {self.HP}
Level: {self.LVL}
""")
        input()
        clear()
    def display_inventory(self):
        clear()
        if self.INV:
            for item in self.INV:
                printer(f"Weapon {self.INV.index(item) + 1}: {item.weapon} - Weapon strength: {item.weaponstr}")
                print()
            printer("Enter the number to the corresponding weapon if you wish to equip it, if not just press enter.")
            equip = input()
            for item in self.INV:
                if str(self.INV.index(item) + 1) == equip: 
                    item.equip()
        else:
            printer("You poor")
        input()
        clear()

class Monster():
    def __init__(self):
        self.dif = 0
        self.STR = 0
    def dif_up(self):
        self.dif += 1
        printer("Monsters are now even stronger. ")
    def monster_fight(self):
        self.STR = r.randint(1, 10) + self.dif

class Item():
    def __init__(self, weapon, weaponstr):
        self.weapon = weapon
        self.weaponstr = weaponstr
        self.equiped = False
    def equip(self):
        clear()
        for item in player.INV:
            if item.equiped:
                player.STR -= item.weaponstr
                item.equiped = False
        self.equiped = True
        player.STR += self.weaponstr
        printer(f"You equiped {self.weapon} and recieved {self.weaponstr} extra strength giving you the total strength of {player.STR}.")
        
player = Player()
monster = Monster()
potion_counter = 0
has_potion = False

door_alt = ["trap","monster","chest"]
alive = True

#Detta är alla vapen som finns.
item1 = Item("Battle Axe", 1)
item2 = Item("Cock Sword", 2)
item3 = Item("Handheld Ballista", 3)
item4 = Item("Martin", 4)
item5 = Item("Curtain Rod", 5)
item6 = Item("Slingshot", 6)
item7 = Item("Ball", 7)
item8 = Item("Ak5C", 8)
item9 = Item("Garden Gnome", 9)
item10 = Item("Golf Club", 10)
item11 = Item("Panzer VIII Maus", 64)

item_list = [item1,item2,item3,item4]

while True: #Game loop
    if player.HP <= 0:
        printer("YOU DIED *omnious death sound")
        alive = False
        break
    if player.LVL == 10:
        printer("You win!")
        alive = False
        break
    if alive:
        clear()
        printer("""
MENU: (Type the number that correspondes to the action you wish to do)
1 - Open some doors
2 - Display some stats
3 - View some inventory
""")
        choice = input()
        if choice == "1":
            clear()
            open_door(potion_counter, has_potion)
        elif choice == "2":
            clear()
            player.display_stats()
        elif choice == "3":
            player.display_inventory()
        elif choice == "amogus":
            player.HP = 101
        else:
            clear()
            printer("You have to write a number 1-3 sir / madame. ")
            input()

