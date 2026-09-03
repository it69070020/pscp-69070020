"""CATCH HIM!....HER!....THEM?....wait what?"""
def main():
    """Egao de hodashitara mayowazu Kill Kodoku na Shadow Shadow"""
    n = input()
    n_splited = n.split()
    N = int(n_splited[0])
    K = int(n_splited[1])
    T = int(n_splited[2])
    ppl = 1
    count = 1
    if ppl == T:
        print(count)
        return

    for _ in range(N):
        ppl = (ppl - 1 + K) % N + 1
        if ppl == 1:
            break
        count += 1
        if ppl == T:
            break
    print(count)
main()
