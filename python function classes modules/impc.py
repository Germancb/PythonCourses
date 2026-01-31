import collections   #impc python corre
import random
rank=[]
for i in range(2,11):
    rank.append(str(i))
let=["J","Q", "K", "A"]
for x in let:
    rank.append(x)
suits= ['Spades', 'Diamonds', 'Hearts', 'Clubs']


print(rank)
Pcard=collections.namedtuple('card', ['suit', 'rank'])

class Pdc:
#   ranks=[str(rank) for rank in range(2,11)]+ ["J","Q", "K", "A"]
#    suits= ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    def __init__(self):
        self._cards=[Pcard(rank, suit) for suit in suits]
#        sc=[Pcard(rank, suit) for suit in self.suits]   #si suits va dentro de class lin 17
        print(self._cards)
#       print(Pcard)
#   return self._cards
p2=Pdc()
print(p2._cards)



