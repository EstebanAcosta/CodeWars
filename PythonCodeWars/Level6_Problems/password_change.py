# Author: Esteban Acosta
#A passphrase is like a password, but is generally longer, and used for added security. 
#They are often taken from poems, songs, movie names and so on. 
#However, they can often be guessed due to common cultural references. 
#One way to make a passphrase more secure is to encode it before use.

# Consider the following encoding:

# 1 - Shift each letter by a given number. Make sure to consider circular shifting, so 'z' should become 'a' when shifted forward.
# 2 - Replace each digit with its complement to 9.
# 3 - All non-alphabetic and non-digit characters can be left as is.
# 4 - Any letter at an odd index should be lowercase, while any letter at an even index should be uppercase.
# 5 - Take the entire string, and reverse it.

# For Example:
# Starting with "BORN IN 2015!", with a shift of 1:

# 1 - "CPSO JO 2015!"
# 2 - "CPSO JO 7984!"
# 3 - "CPSO JO 7984!"
# 4 - "CpSo jO 7984!"
# 5 - "!4897 Oj oSpC"

# With longer passphrases, it is better to have a small program to help create it. Can you create this program?

def play_pass(s, n):
    passw = []
    for i in range(len(s)):
        if s[i].isdigit():
            passw.append(str(abs(9 - int(s[i]))))
            
        elif s[i].isalpha():
            char = s[i]
            j = 0
            while j < n:
                if char == "z":
                    char = "a"
                    j+=1
                    continue
                elif char == "Z":
                    char = "A"
                    j+=1
                    continue
                    
                char = chr(ord(char) + 1) 
                j+=1
                         
            if i%2 == 0:
                char = char.upper()
            else:
                char = char.lower()
            passw.append(char)
        else:
            passw.append(s[i])
    
    return "".join(passw)[::-1]
            
            