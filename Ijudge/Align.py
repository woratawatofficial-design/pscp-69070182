"""Align"""
def main():
    """This function gives you an alignment of your text"""
    X = int(input())
    direction = input().lower()
    word = input()
    AREA = X - len(word)
    if direction == 'left':
        print(word + " "*AREA)
    elif direction == 'right':
        print(AREA*' ' + word)
    else:
        if AREA % 2:
            print(" "*((AREA//2)+1) + word + " "*(AREA//2) )
        else:
            print(" "*(AREA//2) + word + " "*(AREA//2))
main()
