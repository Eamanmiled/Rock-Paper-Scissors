import random, time

def game(userinp, npcinp):
    if userinp == 1 and npcinp == 2:
        print("npc win")
    elif userinp =


print("hello this is my rock paper scissors game\nyou may type either of those three options or \n1\n2\n3\n"
      "to play your hand\nenter anything to begin.")
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
choices = ["1", "2", "3", "rock", "paper", "scissors"]
choice = input("what do you choose: ")
while choice != "run away":
    npcchoice = choices[random.randint(0, 5)]
    if choice not in choices:
        choice = input("choose 1,2,3 or rock, paper, scissor please")
    else:
        game(choice,npcchoice)
        choice = input("what do you choose to play now or run away?")

print("thanks for playing dawg")
