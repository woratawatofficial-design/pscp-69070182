"""Meteorite"""
def main():
    """This function calculates the total shots"""
    weight = float(input())
    piece = int(input())
    victory = float(input())
    total_shots = 0
    TIMES = 0
    if weight and weight > victory:
        weight = weight / piece
        total_shots += 1
        TIMES += 1
    while weight >= victory:
        weight = weight/piece
        total_shots += piece**TIMES
        TIMES += 1
    print(total_shots)
main()
