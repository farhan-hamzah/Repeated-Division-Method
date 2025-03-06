def sumBase(n: int, k: int) -> int:
    total = 0
    while n > 0:
        total += n % k
        n //= k        
    return total

n = int(input())
k = int(input())

print(sumBase(n, k))
