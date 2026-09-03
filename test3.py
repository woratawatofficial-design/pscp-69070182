"""Xmas"""
def xmas():
    """เเย่จัง"""
    C,Q = input().split()
    COLOR = {
        'R':"Red",
        'G':"Green",
        'B':'Blue'
    }
    Q = int(Q)
    for _ in range(Q):
        print(COLOR[C],end =' ')
        if C == 'R':
            C = 'G'
        elif C == 'G':
            C = 'B'
        elif C == 'B':
            C = 'R'
xmas()
