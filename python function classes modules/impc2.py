import collections
import random

Pcard=collections.namedtuple('card', ['suit', 'rank'])

ranks=[str(rank) for rank in range(2,11)]+ ["J","Q", "K", "A"]
suits= ['Spades', 'Diamonds', 'Hearts', 'Clubs']
rank=0
# uit='Spades'
sc=[Pcard(ranks, suit)  for suit in suits]
print(sc)

# S = Student('Nandini', '19', '2541997')

