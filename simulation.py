import itertools


class Round():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1score = 0
        self.player2score = 0 
        self.play()


    def get_winner(self):
        if self.player1score > self.player2score:
            return self.player1
            self.player1.totalwins += 1

        elif self.player2score > self.player1score:
            self.player2.totalwins += 1
            return self.player2
        else:
            return None

    def play(self):
        print(self.player1.name, "is playing", self.player2.name)
        self.player1.createmem(self.player2)
        self.player2.createmem(self.player1)
        for i in range(10):
            desc1 = self.player1.getdescision(self.player2)
            desc2 = self.player2.getdescision(self.player1)
            self.updatescore(desc1, desc2)
        self.player1.totalscore += self.player1score
        self.player2.totalscore += self.player2score
        print(self.player1.name, "got", self.player1score)
        print(self.player2.name, "got", self.player2score)

        




    def updatescore(self, desc1, desc2):
        if desc1 == "cheat" and desc2 == "cheat":
            self.player1.updatemem(self.player2, "cheat")
            self.player2.updatemem(self.player1, "cheat")
            pass

        elif desc1 == "cooperate" and desc2 == "cooperate":
            self.player1score += 2
            self.player1.updatemem(self.player2, "cooperate")
            self.player2score += 2
            self.player2.updatemem(self.player1, "cooperate")

        elif desc1 == "cheat" and desc2 == "cooperate":
            self.player1score += 3
            self.player1.updatemem(self.player2, "cooperate")
            self.player2score -= 1
            self.player2.updatemem(self.player1, "cheat")


        elif desc1 == "cheat" and desc2 == "cooperate":
            self.player1score += 3
            self.player1.updatemem(self.player2, "cooperate")
            self.player2score -= 1
            self.player2.updatemem(self.player1, "cheat")



class Player():


    def __init__(self, name):
        self.name = name

        self.totalwins = 0
        self.mem = {}
        self.totalscore = 0
    

    def updatemem(self, opponent, desc):
        self.mem[opponent.name].append(desc)

    
    def createmem(self, opponent):
        self.mem[opponent.name] = []




class Cooperater(Player):

    def __init__(self, name):
        super().__init__(name)



    def getdescision(self, player):
        return "cooperate"


class Cheater(Player):

    def __init__(self, name):
        super().__init__(name)



    def getdescision(self, player):
        return "cheat"
    


class Titfortat(Player):

    def __init__(self, name):
        super().__init__(name)



    def getdescision(self, player):
        if len(self.mem[player.name]) == 0:
            return "cooperate"
        else:
            return self.mem[player.name][-1]


class Grudge(Player):

    def __init__(self, name):
        super().__init__(name)



    def getdescision(self, player):
        if "cheat" in self.mem[player.name]:
            return "cheat"
        else:
            return "cooperate"

if __name__ == "__main__":
    playerlist = [Cheater("Littlefinger"), Cheater("Khaleesi"), Cheater("Rick"),\
                   Titfortat("Jon Snow"),Grudge("I"), Titfortat("The Mountain"),Titfortat("Arya"),\
                   Cooperater("Sansa"),Cooperater("Tirion"), Cooperater("Ser Davos")]
    matches = itertools.combinations(playerlist, 2)
    for i in matches:

        win = Round(i[0], i[1])


        win1 = win.get_winner()

    for i in playerlist:
        print(i.name, i.totalscore)


    # test3 = Cheater("Khaleesi")
    # test4 = Cooperater("Sansa")
    # win = Round(test3, test4)
    # win1 = win.get_winner()
