""" Problem 17. Letter Combinations of a Phone Number """


def letterCombinations(digits):
    """
    1. base class: when digit =""
    2. If there are still digits to check:iterate over letter to the current combination
       /  |  \
      a   b   c
    / | \
   ad ae af bd be bf cd ce cf

    """
    key_board = {"2": ['a', 'b', 'c'],
                 "3": ['d', 'e', 'f'],
                 "4": ['g', 'h', 'i'],
                 "5": ['j', 'k', 'l'],
                 "6": ['m', 'n', 'o'],
                 "7": ['p', 'q', 'r', 's'],
                 "8": ['t', 'u', 'v'],
                 "9": ['w', 'x', 'y', 'z']}

    def combining(combination, digits):
        # if hit base class
        if len(digits) == 0:
            result.append(combination)
        else:
            for letter in key_board[digits[0]]:
                combining(combination+letter, digits[1:])

    result = []
    if digits:
        combining("", digits)
    return result
