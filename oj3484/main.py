"""Tile Sound"""
def main():
    """Calculate damaged tiles"""
    n, price = map(int, input().split())
    col_tiles = [0] * n
    col_points = [0] * n
    total_tiles = 0
    total_points = 0
    for _ in range(n):
        row = list(map(int, input().split()))
        row_tiles = 0
        row_points = 0
        for j in range(n):
            if row[j] > 0:
                row_tiles += 1
                total_tiles += 1
            row_points += row[j]
            col_tiles[j] += row[j] > 0
            col_points[j] += row[j]

            total_points += row[j]
        print(*row, row_tiles, row_points)
    print(*col_tiles)
    print(*col_points)
    print(total_tiles, total_points, f"{total_points * price:.2f}")
main()
