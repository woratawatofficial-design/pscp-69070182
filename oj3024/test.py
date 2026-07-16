"""Surprising Vote"""
SUM3 = float(input())
HIGH = float(input())
LOW = SUM3 - (HIGH*2)
if LOW < 0:
    LOW = 0
if (HIGH - LOW) > 2:
    print("Surprising")
else: print("Not surprising")
