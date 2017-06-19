import random


def talon_skin_picker():
    choices = {
        1: "Blood Moon",
        2: "Samsung White",
        3: "DragonBlade",
        4: "Renegade",
        5: "Crimson Elite",
        6: "Base"
    }

    skin = random.Random()
    result = skin.randint(1, 6)
    return choices['result']


if __name__ == "__main__":
    print "The Long Sword God Says Use " + talon_skin_picker() + " Talon!"