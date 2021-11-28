import random


def better_coin_flipper(choice):
    coin = random.Random()
    result = coin.randint(0, 1)
    if result:
        print "The almighty conch shell says: '%s'" % (("You should " + choice).title())
    else:
        print "The almighty conch shell says: '%s'" % (("You should not " + choice).title())


if __name__ == "__main__":
    better_coin_flipper("Go to Subway")