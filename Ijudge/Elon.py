"""X-shape"""

def main():
    """This function turns an input into X-shaped output"""
    x, k = input().split()
    x = int(x)

    for i in range(x):
        result = ""

        for j in range(x):
            if i == j or i + j == x - 1:
                if k == "#":
                    result += "#"
                else:
                    result += chr(ord(k) + abs(i - x//2))
            else:
                result += "-"

        print(result)

main()
