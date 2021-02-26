def persistence(n):
    persist = str(n)
    count = 0
    while len(persist) != 1:
        product = 1
        for digit in persist:
            product*=int(digit)
        count+=1
        persist = str(product)
    return count

