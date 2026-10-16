"""TETO LUV BREAD"""
def main():
    """Sonzai shoumei ai datte ai datte haita tte"""
    line1 = input().split()
    W = int(line1[0])
    H = int(line1[1])
    M = int(line1[2])
    N = int(line1[3])

    xs = [0] + list(map(int, input().split())) + [W]
    ys = [0] + list(map(int, input().split())) + [H]

    widths = []
    for i in range(1, len(xs)):
        widths.append(xs[i] - xs[i-1])

    heights = []
    for i in range(1, len(ys)):
        heights.append(ys[i] - ys[i-1])

    widths.sort(reverse=True)
    heights.sort(reverse=True)

    areas = []
    for w in widths[0:2]:
        for h in heights[0:2]:
            areas.append(w * h)

    areas.sort(reverse=True)
    print(areas[0], areas[1])
main()
