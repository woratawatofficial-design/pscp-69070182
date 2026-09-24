"""Rest is what you need"""
def main():
    """this function calculates the time you need
    to finish off your work"""
    WORK = int(input())
    ROUGH = []
    EASY = []
    for HOUR in range(WORK):
        HOUR = int(input())
        if HOUR > 18:
            ROUGH.append(HOUR)
        else:
            EASY.append(HOUR)
    CHECKROUGH = len(ROUGH)
    CHECKEASY = len(EASY)
    LEFT = 0
    TOTAL = 0
    if CHECKROUGH == CHECKEASY:
        TOTAL += CHECKEASY+CHECKROUGH
    elif CHECKROUGH > CHECKEASY:
        LEFT += CHECKROUGH - CHECKEASY
        TOTAL += (2*CHECKEASY) + (LEFT + LEFT-1)
    elif CHECKEASY > CHECKROUGH:
        LEFT += CHECKEASY - CHECKROUGH
        TOTAL += (2*CHECKROUGH) + LEFT
    print(TOTAL)
main()
