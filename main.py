from classes.game import person, bcolors
from classes.magic import spell
from classes.inventory import item



fire = spell("fire", 10, 100, "black")
thunder = spell("thunder", 10, 100, "black")
blizzard = spell("blizzard", 10, 100, "black")
meteor = spell("meteor", 20, 200, "black")
quake = spell("quake", 14, 140, "black")

cure = spell("cure", 12, 120, "white")
cura = spell("cura", 18, 200, "white")

potion = item("potion", "potion", "heals 50 HP", 50)
hipotion= item("Hi-potion", "potion", "heals 100 HP", 100)
superpotion = item("Superpotion", "potion", "heals 500 HP", 500)
elixer = item("elixer", "elixer", "fully restores HP/MP of one party member", 9999)
hielixer = item("Megaelixer", "elixer", "fully restores party's HP/MP", 9999)
grenade = item("grenade", "attack", "deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 5}, {"item": grenade, "quantity": 5}]

player1 = person("jack\t\t:", 460, 65, 60, 34, player_spells, player_items)
player2 = person("kim\t\t\t:", 460, 65, 60, 34, player_spells, player_items)
player3 = person("robot\t\t:", 460, 65, 60, 34, player_spells, player_items)
enemy = person("merline :", 1200, 65, 45, 25, [], [])

players = [player1, player2, player3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!!!" + bcolors.ENDC)
while running:
    print("===============================")

    print("\n\n")
    print("NAME\t\t\t                     HP                                     MP")
    for player in players:
        player.get_stats()

    print("\n")

    for player in players:
        player.choose_action()
        choice = input("choose action:")
        index = int(choice)-1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("you attacked for", dmg, "points of damage.Enemy HP:", enemy.get_hp())
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("choose magic:")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNOT ENOUGH MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "heals for", str(magic_dmg), "HP." + bcolors.ENDC)

            elif spell.type == "black":
              enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("choose item:")) - 1

            if item_choice == -1:
                continue
            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "NONE LEFT!!..." + bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP" + bcolors.ENDC )

            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + "fully restores HP\MP" + bcolors.ENDC)

            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + "deals", str(item.prop), "points of damage " + bcolors.ENDC)





    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("enemy attacks for", enemy_dmg, "player HP", player.get_hp())
    print("---------------------------------")
    print("enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC+"\n")

    if enemy.get_hp()==0:
        print(bcolors.OKGREEN + "YOU WIN!!!" + bcolors.ENDC)
        running = False

    elif player.get_hp()==0:
        print(bcolors.FAIL + "your enemy has DEFEATED YOU:(" + bcolors.ENDC)
        running = False


