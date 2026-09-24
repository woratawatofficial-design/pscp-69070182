"""Cinema"""
def main():
    """Cinema yuri date"""
    total = int(input())
    while total > 0:
        age,amount = map(int,input().split())
        total -= amount
main()