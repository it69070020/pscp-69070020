"""Imma plant some flower to fight zombies"""
def main():
    """Omoi no bouken o Wasurezu ni zenbu ieru kana?"""
    info = input().split()
    L = int(info[0])
    N = int(info[1])

    m = 1
    while True:
        k = m * L
        total = k * (k + 1) // 2
        if total >= N:
            print(m)
            break
        m += 1
main()
