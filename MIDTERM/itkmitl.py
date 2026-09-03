"""CHeckLINK"""
PREFIX = "https://ijudge.it.kmitl.ac.th/problems/"

X = input()

if not X.startswith(PREFIX):
    print("INVALID")
else:
    code = X[len(PREFIX):]

    code = code.rstrip("/")

    if len(code) == 4 and code.isdigit():
        print(code[0] + " STAR")
    else:
        print("INVALID")