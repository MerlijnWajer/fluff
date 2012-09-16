
class Keeper(object):
    def __init__(self, name):
        self.name = name

    def execCard(self):
        print "Player %s played keeper %s" % \
            (game.xs_turn.name, self.name)
        game.xs_turn.keepers.append(self)

keepers = [Keeper(name) for name in [
    "Brain, The",
    "Bread",
    "Chocolate",
    "Cookies",
    "Cosmos, The",
    "Dreams",
    "Eye, The",
    "Love",
    "Milk",
    "Money",
    "Moon, The",
    "Peace",
    "Rocket, The",
    "Sleep",
    "Sun, The",
    "Television",
    "Time",
    "Toaster, The",
    "Party, The"
    ]

class NewRule(object):
    def __init__(self, name, descr):
        self.name = name
        self.descr

    def execCard(self):
        print "Player %s played a new rule %s" % \
            (game.xs_turn.name, self.name)
        print "----------"
        print self.descr
        game.self.rules.append(self)

    def onEnterGame(self):
        pass

    def onLeaveGame(self):
        pass

    def execRule(self):
        raise NotImplementedError("Override me! :(")

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

class PlayX(NewRule):
    def __init__(count):
        NewRule.__init__("Play %d" % count,
        """
Players draw %d cards on the start of their turn.
        """ % count)
        self.count = count

    def execRule(self):
        for i in xrange(count):
            game.xs_turn.hand.append(game.drawCard())

Play2, Play3, Play4 = [PlayX(i) for i in xrange(2,5)]
class Game(object):
    def __init__(self, players, deck):
        # XXX Shuffle deck?
        self.players = players
        self.deck = deck
        self.trash = []
        self.xs_turn = players[0]
        self.xs_count = 0

    def nextTurn(self):
        self.xs_count = (1 + self.xs_count) % len(self.players)
        self.xs_turn = self.players[self.xs_count]

    def startTurn(self):

    def setupGame(self):
        for _ in xrange(len(self.players)):
            for _ in xrange(3):
                self.xs_turn.hand.append(self.drawCard())
            self.nextTurn()

    def drawCard(self):
        if not self.deck:
            pass
            # Shuffle trash into deck
        return self.deck.pop(0)

    def discardCard(self, card):
        self.trash.append(card)

    def playCard(self, card):
        card.execCard()
        self.trash.append(card)

class Player(object):
    pass

