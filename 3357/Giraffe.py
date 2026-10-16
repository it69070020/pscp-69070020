"""CUT THEIR HEAD"""
def main():
    """Kizuite yo Rishuu shite yo Atashi no koto ton ton Moo, bee!"""
    info = [0]
    n = int(input())
    for _ in range(n):
        height = int(input())
        info.append(height)
    info.append(0)
    count = 0
    for i in range(1, n+1):
        if info[i] > info[i-1] and info[i] > info[i+1]:
            count += 1
    print(count)
main()
