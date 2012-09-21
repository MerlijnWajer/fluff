
from random import shuffle
import sys

class Card(object):
    def on_draw():
        """
        Call upon drawing from deck.
        """
        raise NotImplementedError("Override me :(")

    def on_play()
        """
        Call upon coming into play.
        """
        raise NotImplementedError("Override me :(")

    def on_remove():
        """
        Call upon removal from play.
        """
        raise NotImplementedError("Override me :(")

    def on_discard():
        """
        Call upon removal from hand.
        """
        raise NotImplementedError("Override me :(")

class Keeper(Card):
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
    ]]

class NewRule(Card):
    def __init__(self, name, descr):
        self.name = name
        self.descr = descr

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

    def classify():
        """
        Returns exclusive rule class, only a single cards
        of a certain rule class may be into play at a given time.
        The only exception is the None class.
        """

        return None

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

class BasicRules(NewRule):
    def __init__(self):
        NewRule.__init__(self, "Basic rules",
            "Draw 1 card, Play 1 card")

    def on_draw():
        pass

    def on_play():
        pass

    def on_discard():
        pass

    def execRule(self):
        game.xs_turn.hand.append(game.drawCard())
        game.xs_turn.doAction("Play a card")

class DrawX(NewRule):
    def __init__(self, count):
        NewRule.__init__(self, "Draw %d" % count,
        """
Players draw %d cards on the start of their turn.
        """ % count)
        self.count = count

    def execRule(self):
        # -1 because the basic rules will inforce
        # a draw
        # XXX: Change later with respect to inflation?
        for i in xrange(count - 1):
            game.xs_turn.hand.append(game.drawCard())

    def classify(self):
        return 'draw'

Draw2, Draw3, Draw4 = [DrawX(i) for i in xrange(2,5)]

class Game(object):
    # XXX: Maybe add support for "tables"
    # which represent the global context all players can see
    def __init__(self, players, deck):
        self.players = players
        shuffle(deck)
        self.deck = deck
        self.trash = []
        self.rules = []
        self.xs_turn = players[0]
        self.xs_count = 0

    def next_player(self):
        self.xs_count = (1 + self.xs_count) % len(self.players)
        self.xs_turn = self.players[self.xs_count]

    def start_turn(self):
        print "Player %s's turn" % self.xs_turn.name
        for rule in self.rules:
            rule.execRule()

    def run(self):
        self.setup_game()

        while True:
            self.next_player()
            self.start_turn()

    def setup_game(self):
        # Deal the initial cards
        for _ in xrange(len(self.players)):
            for _ in xrange(3):
                self.xs_turn.hand.append(self.drawCard())
            self.next_player()

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
    def __init__(self, name):
        self.name = name
        self.hand = []

    def doTurn(self):
        raise NotImplementedError("Override me too :(")

class ShellPlayer(Player):
    def issue(self):
        print "Your turn player", self.name

    def pick_yesno(self, action):
        pass

    def pick_num(self, action):
        print action
        print "There are %d cards in your hand:" % len(self.hand)

        for card in self.hand:
            print card

        self.playCard()

    def drawCard():
        print "You draw a card"
        self.hand.append(game.drawCard())
        print self.hand[-1]

    def playCard()
        print "Pick a card to play"

        while True:
            try:
                num = int(sys.stdin.readline().strip())

                if num < 0:
                    raise ValueError("too low")

                if num >= len(self.hand):
                    print "That number is too high"
                    continue

                break

            except ValueError:
                print "Invalid number"

        card = self.hand.pop(num)
        game.playCard(card)

deck = keepers

players = [ShellPlayer(x) for x in ["Foo", "Bar", "Baz", "Quux"]]

game = Game(players, deck)
game.run()

