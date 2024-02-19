Player_info = r"C:\Users\luizg\OneDrive\Documentos\Project\Text Game\Player Info.txt"
enemy = {"HP": 0, "Attack": 0, "Defense": 0, "lvl": 0, "Item": {}}

#Reads Player info
def Read_Player(Player_info):
    import json
    with open(Player_info, "r") as Player_info:
        content = Player_info.read()
    Player = json.loads(content)
    return Player

#Creation of random enemies of any level
def Enemy_Creation(enemy, lvl):
    import random
    enemy["HP"] = random.randint(4*(lvl/2), 10*(lvl/2))
    enemy["Attack"] = random.randint(2*(lvl/2), 4*(lvl/2))
    enemy["Defense"] = 2*(lvl/2)
    enemy["lvl"] = lvl
    return enemy

#Battle system
def Battle_System(Player, enemy, enemy_name):
    while Player["HP"] > 0 and enemy["HP"] > 0:
        defense_points_player = 0
        defense_points_enemy = 0
        choise = ""
        while choise.upper() not in ["A", "D"]:
            choise = input("\nChoose ATTACK[A] or DEFEND[D]: ")
            if choise.upper() == "A":
                enemy["HP"] -= Player["Attack"]
                break
            elif choise.upper() == "D":
                defense_points_player += Player["Defense"]
                break
            else:
                print("Please enter a valid option.")

        if enemy["HP"] <= 0:
            break
        import  random
        enemy_choise = random.randint(0, 1)
        if enemy_choise == 0: Player["HP"] = max(0, Player["HP"] + defense_points_player - enemy["Attack"])
        else:
            defense_points_enemy += enemy["Defense"]
            enemy_damage = max(0, enemy["Attack"] - defense_points_player)
            #Player["HP"] = max(0, Player["HP"] - enemy_damage)

        print(f"\nPlayer HP: {Player['HP']}")
        print(f"Enemy HP: {enemy['HP']}")

    if Player["HP"] <= 0:
        print("Player has been defeated by the {}.".format(enemy_name))
        result = False
        return result
    else:
        print("The {} has been defeated.".format(enemy_name))
        result = True
        return result

#shows to the player his status
def Show_Player_Status(Player):
    print("\n\n[PLAYER STATUS]\nCurrent HP: {}\nCurrent Defense: {}\nCurrent Attack: {}".format(Player["HP"], Player["Defense"], Player["Attack"]))


#Driver
while True:
    print("Welcome to the Text Advanture Game!!!\n"
          "----------------------------------------------\n"
          "--@@@@@@@------@@------@@------@@-----@@@@@@@-\n"
          "-@-----------@@--@@----@@@@-@@@@@-----@-------\n"
          "-@---@@@@@---@@--@@----@@-@@@--@@-----@@@@@@@-\n"
          "-@------@----@@@@@@----@@------@@-----@-------\n"
          "--@@@@@@-----@----@----@@------@@-----@@@@@@@-\n"
          "----------------------------------------------\n\n")
    input("[PRESS ENTER TO CONTINUE]")
    Player = Read_Player(Player_info)
    print("The king has demanded that you go after the great Oger to be defeated!\n"
          "Take care! For this enemy is greater than you may think!\n\n")
    print("You get to the magic forest. Everything is calm and quiet.. until...\n"
          "from behind a tree you see the great blob of green flesh and muscle\n"
          "It is him... the great Oger! Prepare yourself!")
    enemy = Enemy_Creation(enemy, 1)
    print("HP: {}\n"
          "------------___--------\n"
          "-------__--/ ..\-------\n"
          "------|--|-\ <>/--@----\n"
          "-------\/@@/O O\@@-----\n"
          "-----------\___/-------\n"
          "----------_/---\_------\n"
          "Attack: {}---Defense: {}".format(enemy["HP"], enemy["Attack"], enemy["Defense"]))
    result = Battle_System(Player, enemy, "Oger")
    if result == False:
        print("You failed, the king is disappointed")
        str = input("\nYou would like to play again? [Y/N]: ")
        if str[0].upper() != "Y":
            print("\n\nThanks for Playing!!!")
            break
    Show_Player_Status(Player)
    print("\n\nCongratulations, you defeated the Oger!\n"
          "Now the king requests you to see you.\n"
          "As you get to the castle, all people cheer you up. Flower petals are thrown at you\n"
          "Then, the king says 'Congratulation adventurer, now I need you to defeat the Big Boar!'\n"
          "So you went your way to the Black Forest, where the Big Boar resides, according to the map\n"
          "provided to you\n"
          "Suddenly, you see a shadow appear in front of you, it is him, the Big Boar!\n")
    enemy = Enemy_Creation(enemy, 5)
    print("HP: {}\n"
          "-----------------------\n"
          "-------__________------\n"
          "------/|        ..\----\n"
          "-----@-|  B  B    ^^---\n"
          "-------|_________/-----\n"
          "-------|---------|-----\n"
          "Attack: {}---Defense: {}".format(enemy["HP"], enemy["Attack"], enemy["Defense"]))
    result = Battle_System(Player, enemy, "Big Boar")
    if result == False:
        print("You failed, the king is disappointed")
        str = input("\nYou would like to play again? [Y/N]: ")
        if str[0].upper() != "Y":
            print("\n\nThanks for Playing!!!")
            break
    Show_Player_Status(Player)
    print("\n\nCongratulations, you defeated the Big Boar!\n"
          "Now the king requests you to see you one las time, and he looks scared.\n"
          "As you get to the castle, the king leaves the throne and rushes to you\n"
          "Then, the king says 'Adventurer! I am happy to see that you have been victorious, but\n"
          "now I have an emergency that I need you to resolve, urgently!'\n"
          "Before you are able to ask, the king completes: 'My daughter, she was kidnapped\n"
          "by the Red Dragon, the one that has been evading taxes and now he is upset because I took\n"
          "his stocks and bonds to pay for the missing taxes. Please, kill him and kill that tax eva... I mean, my"
          "daughter I mean... if you rescue her, ou can marry her. or whatever, so go!'\n"
          "So, taken by the spirit of heroism and tax responsibility, you go towards the Big Mountain\n"
          "There it was, the Red Dragon, full of range, upset for having his income taxes yearly by the king\n")
    enemy = Enemy_Creation(enemy, 8)
    print("HP: {}\n"
          "--------------------------------------------------------\n"
          "-------___________-----A^__^A-----___________-----------\n"
          "------/  .  .     \---/ $  $ \---/           \----------\n"
          "-----/_________.  .\--\  ..  /--/    _________\---------\n"
          "---------------\   .\__\V__V/__/____/-------------------\n"
          "--------------__\___/          \___/__------------------\n"
          "-------------|                        |------HELP!------\n"
          "--------------\    >            <    /------/-----------\n"
          "---------------VVVV              VVVV-----.o.-----------\n"
          "------------------|              |--------/|\-----------\n"
          "----------------___\            /___----___|\___--------\n"
          "--------------_/    \          /    \_-/        \__-----\n"
          "------------</      /          \      \>           \----\n"
          "Attack: {}---Defense: {}".format(enemy["HP"], enemy["Attack"], enemy["Defense"]))
    result = Battle_System(Player, enemy, "Red Dragon")
    if result == False:
        print("You failed, the king is disappointed")
        break
    else:
        print("Congratualations! You saved the princess, married her, and now you have two cats and thee babies\n"
              "-----------------------\n"
              "---------o-.o.---------\n"
              "------o-/|\/|\-o-o-----\n"
              "--o~~-|-/|-/|--|V|-o~~-\n")
        str = input("\nYou would like to play again? [Y/N]: ")
        if str[0].upper() != "Y":
            print("\n\nThanks for Playing!!!")
            break
    break