import random

class StrikeBall:

    def __init__(self):
        self.secret = []
        self.digits = 0
        self.trials = 0
        self.strike_trials = 0

    def newGame(self, count):
        self.secret = []
        self.digits = count
        for i in range(self.digits):
            r = random.randint(1, 9)
            while r in self.secret:
                r = random.randint(1, 9)
            self.secret.append(r)
        self.trials = 0
        self.strike_trials = 0

    def guess(self, userGuess):
        self.trials += 1
        strikes, balls = 0, 0
        strikesSet = set()
        g = [int(x) for x in userGuess]
        for i in range(self.digits):
            if g[i] == self.secret[i]:
                strikes += 1
                self.strike_trials += 1
                strikesSet.add(g[i])
                if strikes == 2 :
                    self.strike_trials -= 1
                elif strikes == 3:
                    self.strike_trials -= 1
        if strikes == 0 :
            self.strike_trials = self.strike_trials
        for i in range(self.digits):
            if g[i] not in strikesSet and g[i] in self.secret:
                balls += 1
        return strikes, balls

    def getGuessCount(self):
        return self.trials

    def getGuessCount1(self):
        return self.strike_trials

    def hint(self):
        r = random.randint(0,3)
        return self.secret[r]

    def answer(self):
        return self.secret[0]*100+self.secret[1]*10+self.secret[2]

if __name__ == '__main__':
    s = StrikeBall()
    count = 3
    s.newGame(count)
    strikes = 0
    while strikes < count:
        inputString = int(input("Your guess: "))
        while len(inputString) != count:
            print("Input %d digits!" % count)
            inputString = int(input("Your guess: "))
        if inputString == "0" * count:
            print(s.secret)
        strikes, balls = s.guess(inputString)
        print("%d strike(s), %d ball(s)" % (strikes, balls))

    guessCount = s.getGuessCount()
    print("SUCCESS in %d trials" % guessCount)
