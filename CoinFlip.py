import random

def cointoss():
    coin = ["Heads","Tails"]
    return random.choice(coin)

while(True):
    choice = input("Press enter to flip the coin, press e and enter to exit: ")
    if(choice != "e"):
        print("You flipped", cointoss())
    else:
        break

print("Thanks for playing and have a great day")
