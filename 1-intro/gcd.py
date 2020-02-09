### CALCULATE GCD(M,N) ###

## SOLUTION 1
def euclid(m,n):
    while n != 0:
        r = m % n
        m = n
        n = r 
    return m

## SOLUTION 2
def search(m,n):
    t = min(m,n)
    while t > 0:
        if m%t==0 and n%t==0:
            return t
        t -= 1
    return -1


print(euclid(24, 10))
print(search(24, 10))