# fragmenty dotyczące rozwiązania poszczególnych zadań proszę oddzielić odpowiednimi komentarzami

from array import *
import random
import numpy

### zad. 2 ###

# arr = array('u')
# print("Wprowadź znak, jeśli wprowadzisz liczbę znaków różną od 1 zakończysz"
#       "działanie programu")
# char = input("Wprowadź znak ")
# while len(char) == 1:
#     arr.append(char)
#     char = input("Wprowadź znak ")
#
# arr.reverse()
#
# for i in arr:
#     print(i)

### zad. 3 ###

# array = array('i')
#
# with open("result.txt", "w") as file:
#     for i in range(10):
#         array.append(random.randint(-5, 5))
#         file.write(str(array[i]) + " ")

### zad. 4 ###


# def duobleArray():
#     nArray = numpy.arange(2, 7)
#     nArray1 = numpy.append([nArray], [nArray**2], 0)
#     nArray1 = numpy.append([nArray], nArray1**2, 0)
#     nArray1 = numpy.append([nArray], nArray1**2, 0)
#     nArray1 = numpy.append([nArray], nArray1**2, 0)
#     print(nArray1)
#
#
# duobleArray()


### zad. 5 ###


# def histogram(file):
#     dic = {}
#     with open(file, "r") as f:
#         for char in f.read():
#             if char in dic:
#                 dic[char] += 1
#             else:
#                 dic[char] = 1
#     print(dic)
#
#
# histogram("plik.txt")


### zad. 6 ###

deckOfCards = []
ranga = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
kolor = ['c', 'd', 'h', 's']

for i in ranga:
    for j in kolor:
        deckOfCards.append('(' + ','.join([i, j]) + ')')


def show(deck):
    for i in deck:
        print(i)


def deck(deck):
    deck.sort()
    show(deck)


def deal(deck, n):
    cards = []
    for player in range(0,n):
        tab = []
        for card in range(0,5):
            tab.append(deck.pop())
        cards.append(tab)
    return cards


def shuffle_deck(deck):
    random.shuffle(deck)
