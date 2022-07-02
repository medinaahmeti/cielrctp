def CIELRCPT(n): 
    prices=11
    total=0
    while n != 0: 
        if n / 2**prices >= 1:
            n -= 2**prices
            total += 1
        else: 
            prices -= 1
    return total

t = int(input())
for i in range(t):
    n = int(input())
    answer = CIELRCPT(n)
    print(answer)
