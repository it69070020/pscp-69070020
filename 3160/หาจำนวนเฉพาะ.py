"""Find prime numbber"""
def main(n):
    """mirai o soujuu dekiru no wa sekaijuu de tatta hitori da"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

first, last = map(int, input().split())

prime = []
for num in range(first, last + 1):
    if main(num):
        prime.append(num)

if prime:
    print(*prime)
print(f"Total primes: {len(prime)}")
