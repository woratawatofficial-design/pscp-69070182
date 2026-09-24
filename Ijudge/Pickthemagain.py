"""PickThemAgain"""
def main():
    """She's a runner she's a trackstar, she gon run away when it gets hard."""
    X = list(input().split())
    result = []
    for i in X:
        if not int(i) % 3 or not int(i) % 5:
            result.append(i)
    if not result:
        print("Nope")
    for j in result[::-1]:
        print(j)
main()
