import operator

__author__ = 'Daniel'


class Troop(object):
    def __init__(self, elixirCost, trainingTime):
        self.elixirCost = elixirCost
        self.trainingTime = trainingTime


class Barbarian(Troop):
    def __init__(self):
        super(Barbarian, self).__init__(elixirCost=150.0, trainingTime=20)

    def __str__(self):
        return "Barbarian"


class Archer(Troop):
    def __init__(self):
        super(Archer, self).__init__(elixirCost=300.0, trainingTime=25)

    def __str__(self):
        return "Archer"


class Giant(Troop):
    def __init__(self):
        super(Giant, self).__init__(elixirCost=2250.0, trainingTime=2 * 60)

    def __str__(self):
        return "Giant"


class Goblin(Troop):
    def __init__(self):
        Troop.__init__(self, elixirCost=100.0, trainingTime=30)

    def __str__(self):
        return "Goblin"


class WallBreaker(Troop):
    def __init__(self):
        Troop.__init__(self, elixirCost=3000.0, trainingTime=2 * 60)

    def __str__(self):
        return "WallBreaker"


class Balloon(Troop):
    def __init__(self):
        super(Balloon, self).__init__(elixirCost=4000.0, trainingTime=8 * 60)

    def __str__(self):
        return "Balloon"


class Wizard(Troop):
    def __init__(self):
        super(Wizard, self).__init__(elixirCost=3500.0, trainingTime=8 * 60)

    def __str__(self):
        return "Wizard"


class Healer(Troop):
    def __init__(self):
        Troop.__init__(self, elixirCost=8000.0, trainingTime=15 * 60)

    def __str__(self):
        return "Healer"


class Dragon(Troop):
    def __init__(self):
        Troop.__init__(self, elixirCost=33000.0, trainingTime=30 * 60)

    def __str__(self):
        return "Dragon"


class Pekka(Troop):
    def __init__(self):
        Troop.__init__(self, elixirCost=36000.0, trainingTime=45 * 60)

    def __str__(self):
        return "Pekka"


def main():
    # See which troops expends more elixir per second.
    barb = Barbarian()
    arch = Archer()
    giant = Giant()
    gob = Goblin()
    # We ignore wall breakers...
    ball = Balloon()
    wiz = Wizard()
    heal = Healer()
    drag = Dragon()
    pek = Pekka()

    troops = {barb, arch, giant, gob, ball, wiz, heal, drag, pek}
    troopsMap = {}
    for troop in troops:
        troopsMap[troop.elixirCost / troop.trainingTime] = str(troop)

    sortedTroopsMap = sorted(troopsMap.items(), key=operator.itemgetter(0))

    print sortedTroopsMap

if __name__ == '__main__':
    main()
