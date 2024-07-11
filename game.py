import random, time, os


#-------------------------------- function section
def game(userinp, npcinp):
    global wins, losses, draws
    if (userinp == "rock" and npcinp == "paper" or userinp == "paper" and npcinp == "scissor"
            or userinp == "scissor" and npcinp == "rock"):
        print("npc win")
        losses += 1
    elif userinp == npcinp:
        print("Draw")
        draws += 1
    else:
        print("player win")
        wins += 1


def art(move):
    if move == "rock":
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif move == "paper":
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    else:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)


#-------------------------------- narrative section
print("hello this is my rock paper scissors game\nyou may type either of these three options"
      " to play your hand\nenter anything to begin.")
input()
print("------------------------------------------------------------")
time.sleep(2)
print("You find yourself in a dark, damp dungeon, the air thick with the smell of moss and\n"
      "something  you can't quite place... maybe dragon breath?\n"
      "You hear a low growl and turn around, your heart racing. A massive monster emerges from\n"
      "the shadows, its eyes glowing with an eerie light. You brace yourself for an attack,\n"
      "gripping your sword tightly.\n")
input("press anything to continue")
print("But then, to your utter surprise, the monster stops just a few feet away. It tilts its\n"
      "head, then slowly extends one of its giant claws.\n"
      "You blink in confusion as the monster gestures for... a handshake? No, wait... it's\n"
      "gesturing to play rock-paper-scissors!\n"
      "You laugh nervously, unsure of what to do. But, hey, if a monster wants to play a game,\n"
      "who are you to refuse?\n"
      "With a sigh of relief, you put away your sword and get ready for the most intense\n"
      "rock-paper-scissors match of your life.\n")

#-------------------------------- gameplay section
wins = 0
losses = 0
draws = 0

if os.path.exists("game_stats.txt"):
    with open("game_stats.txt", "r") as file:
        stats = file.readlines()
        if len(stats) == 3:
            wins = int(stats[0].strip())
            losses = int(stats[1].strip())
            draws = int(stats[2].strip())

choices = ["rock", "paper", "scissor"]
choice = input("what do you choose: ")
while choice != "run away":
    npcchoice = choices[random.randint(0, 2)]
    if choice not in choices:
        choice = input("choose rock, paper or scissor please: ")
    else:
        print("you chose", choice)
        art(choice)
        time.sleep(2)
        print("Monster chose", npcchoice)
        art(npcchoice)
        time.sleep(2)
        game(choice, npcchoice)
        choice = input("what do you choose to play now or run away: ")

#-------------------------------- end section
print(
    "                        ,////,\n"
    "                        /// 6|\n"
    "                        //  _|\n"
    "                       _/_,-'\n"
    "                  _.-/'/   \\   ,/;,\n"
    "               ,-' /'  \\_   \\ / _/\n"
    "               `\\ /     _/\\  ` /\n"
    "                 |     /,  `\\_/\n"
    "                 |     \\'\n"
    "    /\\_        /`      /\\\n"
    "   /' /_``--.__/\\  `,. /  \\\n"
    "  |_/`  `-._     `\\/  `\\   `.\n"
    "            `-.__/'     `\\   |\n"
    "                          `\\  \\\n"
    "                            `\\ \\\n"
    "                              \\_\\__\n"
    "                               \\___)\n")
print("Thanks for playing dawg")

with open("game_stats.txt", "w") as file:
    file.write(f"{wins}\n{losses}\n{draws}\n")
print(f"your wins are: {wins}\nyour losses are: {losses}\nyour draws are: {draws}\n")
