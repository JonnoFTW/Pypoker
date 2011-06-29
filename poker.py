import random

def homo(xs):
    return all(map(lambda x: x == xs[0],xs))
def consec(xs):
    for i in range(len(xs)-1):
        if xs[i+1] != xs[i]+1:
            return False
    return True
class Card:
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

def toval(x):
    cards = {'2':Card.Two,
             '3':Card.Three,
             '4':Card.Four,
             '5':Card.Five,
             '6':Card.Six,
             '7':Card.Seven,
             '8':Card.Eight,
             '9':Card.Nine,
             'T':Card.Ten,
             'J':Card.Jack,
             'Q':Card.Queen,
             'K':Card.King,
             'A':Card.Ace}
    return cards[x]

class Hand:
    def __init__(self,hand):
        self.hand  = hand
        self.suits = self.suits()
        self.vals  = map(toval,self.vals())
        self.vals.sort()
        self.counts =  sorted([(self.vals.count(a),a) for a in set(self.vals)],reverse = True)
    def vals(self):
        return [i[0] for i in self.hand]
    def suits(self):
        return [i[1] for i in self.hand]
    
    def rank(self):
        if homo(self.suits) and self.vals == [Card.Ten,Card.Jack,Card.Queen,Card.King,Card.Ace]:
            return (10,None,"Royal Flush")
        elif homo(self.suits) and consec(self.vals):
            return (9,None,"Straight Flush")
        elif homo(self.vals[1:]) or homo(self.vals[:4]):
            return (8,0,"Four of a Kind")
        elif len(self.counts) == 2:
            return (7,self.counts[0][1],"Full House")
        elif homo(self.suits):
            return (6,max(self.vals),"Flush")
        elif consec(self.vals):
            return (5,max(self.vals),"Full house")
        elif any(map(lambda x: x[0] == 3,self.counts)):
            return (4,filter(lambda x: x[0] == 3,self.counts)[0][1],"3 of a Kind")
        elif len(self.counts) == 3:
            return (3,0,"Two Pair")
        elif len(self.counts) == 4:
            return (2,self.counts[0][1],"One pair")
        else:
            return (1,max(self.vals),"High card")

def winner(p1,p2):
    r1 = p1.rank()
    r2 = p2.rank()
   # if r1[0] != 0 or r2[0] != 0:
    #    print r1,r2
    if r1[0] == r2[0]:
        if r1[1] > r2[1]: return 1
        else: return 2
    if r1[0] > r2[0]: return 1
    else: return 2

scores = dict()
for i in range(100000):
    cards = [i+j for i in "23456789TJQK" for j in "SCHD"]
    random.shuffle(cards)
    h1 = []
    for i in range(5):
        h1.append(cards.pop())
   # print h1
    p1 = Hand(h1)
    try:
        scores[p1.rank()[2]] +=1
    except KeyError:
        scores[p1.rank()[2]] = 1

print scores
