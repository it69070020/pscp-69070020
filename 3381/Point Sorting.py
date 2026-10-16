"""WHY DON'T TELL COPPER GOLEM"""
def main():
    """Akiramete shimau hodo konosaki takusan no"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = []
        for _ in range(n):
            line = input().split()
            x = int(line[0])
            y = int(line[1])
            points.append((x, y))
        points.sort(key=lambda p: (p[0] + p[1], -p[1]))
        for p in points:
            print(p[0], p[1])
main()
