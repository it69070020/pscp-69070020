"""collecting point"""
def main():
    """atari?"""
    n = int(input())
    plus = 0
    minus = 0
    for _ in range(n):
        symbol = input()
        if symbol == "+":
            plus += 1
        else:
            minus += 1

    new_plus = plus * 10
    new_minus = minus * 5
    final = new_plus - new_minus
    print(final)
main()
