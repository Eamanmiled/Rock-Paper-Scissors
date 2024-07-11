import random, time


def game(userinp, npcinp):
    if (userinp == "rock" and npcinp == "paper" or userinp == "paper" and npcinp == "scissor"
            or userinp == "scissor" and npcinp == "rock"):
        print("npc win")
    elif userinp == npcinp:
        print("Draw")
    else:
        print("player win")


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
#begin gameplay
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
print("thanks for playing dawg")
