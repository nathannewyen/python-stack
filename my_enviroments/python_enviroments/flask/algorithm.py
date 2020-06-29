# Let's revisit Generate Coin Change!

# Change is inevitable (especially when breaking a twenty). Make generateCoinChange(cents). Accept a number of American cents, compute and represent that amount with smallest number of coins. Common American coins are pennies (1 cent), nickels (5 cents),dimes (10 cents), and quarters (25 cents).

# Instead of a string, we will return an object/dictionary.
# If the amount of cents was 33, you would return:

# {
#     "Q" : 1,
#     "D" : 0,
#     "N" : 1,
#     "P" : 3
# }

# There are MANY ways to do this algo! Try more than one!


def coinChanges(cents):
    dict = {
        'Q': 0,
        'D': 0,
        'N': 0,
        'P': 0
    }

    dict['Q'] = cents // 25
    cents = cents - (dict['Q']*25)
    dict['D'] = (cents//10)
    cents = cents - (dict['D']*10)
    dict['N'] = cents // 5
    cents = cents - (dict['N']*5)
    dict['P'] = cents
    return dict


print(coinChanges(33))
