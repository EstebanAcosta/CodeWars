import math
def reduceFraction(num,denom):
    while math.gcd(num,denom) != 1:
        gcd = math.gcd(num,denom)
        num/=gcd
        denom/=gcd
        num = int(num)
        denom = int(denom)
    if num < 0 and denom < 0 or num > 0 and denom > 0:
        return str(abs(num)) + "/" + str(abs(denom))
    elif num < 0 or denom < 0:
        return "-" + str(abs(num)) + "/" + str(abs(denom))

def mixed_fraction(s):
    fraction = s.split("/")
    whole = int(int(fraction[0])/int(fraction[1]))
    remain = abs(int(fraction[0]))%abs(int(fraction[1]))
    
    if abs(int(fraction[0])) > abs(int(fraction[1])) and remain != 0:
        return str(whole) + " " +  reduceFraction(remain,abs(int(fraction[1])))
    
    elif abs(int(fraction[0])) < abs(int(fraction[1])) and remain != 0:
        return reduceFraction(int(fraction[0]),(int(fraction[1])))
    
    else:
        return str(whole)