"""BigAhhFrame"""
def main():
    """This function creates a big frame from yo input"""
    A1 = str(input()).strip()
    A2 = str(input()).strip()
    A3 = str(input()).strip()
    A4 = str(input()).strip()
    A5 = str(input()).strip()
    TUP1 = (A1,A2,A3,A4,A5)
    NEW = max(TUP1, key=len)
    max_sentence = "* "+ NEW + " *"
    NEW1 = len(max_sentence)*'*'
    NEWA1 = len(NEW) - len(A1)
    NEWA2 = len(NEW) - len(A2)
    NEWA3 = len(NEW) - len(A3)
    NEWA4 = len(NEW) - len(A4)
    NEWA5 = len(NEW) - len(A5)
    A1 = A1+ ' '*NEWA1
    A2 = A2+ ' '*NEWA2
    A3 = A3+ ' '*NEWA3
    A4 = A4+ ' '*NEWA4
    A5 = A5+ ' '*NEWA5

    print(NEW1)
    print(f"* {A1} *")
    print(f"* {A2} *")
    print(f"* {A3} *")
    print(f"* {A4} *")
    print(f"* {A5} *")
    print(NEW1)
main()
