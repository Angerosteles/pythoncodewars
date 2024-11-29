def sum_strings(x, y):
    #check for empty string, returns 0
    if not x and not y:
        return '0'
    
    #compares lenght of both strings, adjust with zfill, needed to make them same size for zip method
    if len(x) > len(y):
        y = y.zfill(len(x))
    elif len(x) < len(y):
        x = x.zfill(len(y))
    #None carry - thats rest from sum of each index
    #basically were doing "written addition"
    carry = 0
    #result
    badumtsss = []
    #reverse of string and get to list, now we can start addition without iterating from back thats still too abstract 
    #for me
    x = x[::-1]
    y = y[::-1]
    #within loop working on temporary list made within zip, setting proper carry if result > 9, building new list with added up 
    #digits
    for digit_x, digit_y in zip(x, y):
        sum_digits = int(digit_x) + int(digit_y) + carry
        badumtsss.append(str(sum_digits%10))
        carry = sum_digits // 10
    if carry:
        badumtsss.append(str(carry))
    #creating final result group, thats still reversed, so again reversing on join to make string.
    #lastly working on cutting zeros that were left from fill method
    final_badumtsss = ''.join(badumtsss[::-1]) 
    final_badumtsss = final_badumtsss.lstrip('0') or '0'
    
    
    return final_badumtsss

    #first time writing comments

'''

To rozwiązanie mi się podobało bardzo, użycie divmoda

def sum_strings(x, y):
    l, res, carry = max(len(x), len(y)), "", 0
    x, y = x.zfill(l), y.zfill(l)
    for i in range(l-1, -1, -1):
        carry, d = divmod(int(x[i]) + int(y[i]) + carry, 10)
        res += str(d)
    return ("1" * carry + res[::-1]).lstrip("0") or "0"
'''
        


        
