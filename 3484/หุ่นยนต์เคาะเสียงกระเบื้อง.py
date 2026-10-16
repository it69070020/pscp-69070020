"""WHO TF ALLOWED U TO DO THAT CLANKER!"""
def main():
    """ABCD dodoshishirarashishi majikaru mirakuru kuru Pop!"""
    line = input().split()
    n = int(line[0])
    p = float(line[1])
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    col_tiles = [0] * n
    col_points = [0] * n
    total_tiles = 0
    total_points = 0
    for row in grid:
        row_tiles = 0
        row_points = 0
        for j in range(n):
            x = row[j]
            row_tiles = row_tiles + 1 if x > 0 else row_tiles
            row_points = row_points + x
            col_tiles[j] = col_tiles[j] + 1 if x > 0 else col_tiles[j]
            col_points[j] = col_points[j] + x
        print(*row, row_tiles, row_points)
        total_tiles = total_tiles + row_tiles
        total_points = total_points + row_points

    print(*col_tiles)
    print(*col_points)
    print(total_tiles, total_points, f"{total_points * p:.2f}")
main()
