"""
Greedy Solution to the Coin Change Problem
"""

from collections import defaultdict


def change_greedy(amount, coinage):

    coinage = sorted(coinage)
    S = defaultdict(int)
    imax = len(coinage)-1
    output = []
    while amount > 0:
        while coinage[imax] > amount:
            print(coinage[imax])
            imax = imax - 1
        S[coinage[imax]] += 1
        amount -= coinage[imax]
        output.append((imax, S[coinage[imax]]))
    return output
    
print(change_greedy(82, [1, 10, 25, 5]))