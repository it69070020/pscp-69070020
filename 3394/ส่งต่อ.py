"""Just send"""
def main():
    """Wow.. Kon’na sekai to baibaibaibai"""
    line = list(map(int, input().split()))
    n = line[0:1][0]
    s = line[1:2][0]

    foward = [0]
    for _ in range(n):
        foward.append(int(input()))
    seen = set()
    current = s
    while current and current not in seen:
        seen.add(current)
        current = foward[current:current + 1][0]
    print(len(seen))
main()
