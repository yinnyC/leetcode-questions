"""Problems 13. Roman to Integer"""

def romanToInt(s):
    """
    hash -> dict
    
    if cur_value > next_value -> cur_value+next_value
    elif cur_value < next_value -> -cur_value + next_value
    """
    roman_symbols = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    cur_index = 0
    while cur_index < len(s)-1:
        cur_number = roman_symbols[s[cur_index]]
        next_number = roman_symbols[s[cur_index+1]]
        if cur_number < next_number:
            result-= cur_number
        else: 
            result+= cur_number
        print(f'Now Result is {result}')
        cur_index +=1 
    
    result += roman_symbols[s[cur_index]]
    
    return result
            
print(romanToInt('III'))