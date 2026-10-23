"""its not large compare to caseoh"""
def main():
    """Kakaetai koto kanaetai koto Hanaretai koto wasuretai koto"""
    n = int(input())
    r = int(n ** 0.5) + 1
    prime = n > 1
    for i in range(2, r):
        if not n % i:
            prime = False
            break
    if prime is True:
        print("YES")
    else:
        print("NO")
main()
