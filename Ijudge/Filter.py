"""Filter"""
import ast
def main():
    """This function filters students and scores"""
    TXT = ast.literal_eval(input())
    RESULT = []
    minimum = float(input())

    for student, score in TXT.items():
        if score >= minimum:
            RESULT.append((student, score))

    RESULT.sort()

    if not RESULT:
        print("Nope")
    else:
        for student, score in RESULT:
            print(f"{student}\t{score:.2f}")
main()
