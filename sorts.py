# cool sorting algorithms
# by vipe

import random

# sorts:

# bozo sort
def bozo_sort(liste: list, nb: int = 100) -> list:
    """
    this algorithm sorts the list by changing randomly the elements of the list and checking if the list is sorted.
    if after nb tries, the list is still unsorted, it returns -1.
    """
    if liste == [] or len(liste) == 1:
        return liste
    else:
        for i in range(nb):
            l = randomize(liste)
            if check(l):
                return l

        return -1


# bogo sort
def bogo_sort(liste: list, nb: int = 100) -> list:
    """
    this algorithm sorts the list by permuting two random elements and checking if the list is sorted.
    if after nb tries, the list is still unsorted, it returns -1.
    """
    if liste == [] or len(liste) == 1:
        return liste
    else:
        for y in range(nb):
            i = random.randint(0, len(liste) - 1)
            j = random.randint(0, len(liste) - 1)
            liste[i], liste[j] = liste[j], liste[i]
        
            if check(liste):
                return liste
        return -1


# putin sort
def putin_sort(liste: list) -> list:
    """
    this algorithm sorts the list by checking if two following elements are sorted, and deleting the second one when they aren't.
    credits: vladimir putin
    """
    if liste == [] or len(liste) == 1:
        return liste
    else:
        copy = liste[:]
        l = []
        l.append(copy[0])
        for i in range(1, len(copy)):
            if copy[i-1] <= copy[i]:
                l.append(copy[i])
        liste = l
        if check(liste):
            return liste
        else:
            return putin_sort(liste)



# functions:

def randomize(liste: list) -> list:
    copy = liste[:]
    possible_index = [i for i in range(len(liste))]

    for i in copy:
        r = random.choice(possible_index)
        possible_index.remove(r)
        liste[r] = i
    return liste

def check(liste: list) -> bool:
    for i in range(1, len(liste)):
        if liste[i-1] > liste[i]:
            return False
    return True


