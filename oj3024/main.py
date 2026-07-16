"""SurprisingVote"""
SUM3 = float(input())
TOP = float(input())
if TOP <= 10:
    REM = SUM3 - (TOP*2)
    if REM < 0:
        REM = 0
    if (TOP - REM) > 2:
        print("Surprising")
    else: print("Not surprising")
