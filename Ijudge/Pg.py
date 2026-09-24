"""Pig"""
def main():
    """This function gets the larger number from a pair-
    of input, the amount of pair based on the first input"""
    X = int(input())
    Y = list(map(int,input().split()))[:X*2]
    first_position = []
    second_position = []
    for j , z in enumerate(Y, start= 0):
        if not j % 2:
            first_position.append(z)
    for i , k in enumerate(Y, start= 0):
        if i % 2 == 1:
            second_position.append(k)
    for B in range(X):
        if first_position[B] > second_position[B]:
            
main()