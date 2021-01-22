"""Problems 7. Reverse Integer"""

def reverse(self, x: int) -> int:
    """
    reverse integer
    use stack 
    1. handle - sign
    2. handle 0 -> 120 -> 012 start from the first non-zero number
    """
    aStack = []
    answer = 0
    sign = -1 if x<0 else 1

    for digit in str(x*sign):
        aStack.append(digit) # 021
    result = []
    for digit in aStack[::-1]:
        if digit!= 0:
            result.append(digit)
    answer = sign*int("".join(result))

    if answer > (2**31-1) or answer < (-2**31):
        return 0
    else:
        return answer