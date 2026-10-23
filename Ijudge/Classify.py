"""Classify"""

def main():
    """Classify students"""
    mem = []

    while True:
        student = input()
        if student == "END":
            break
        mem.append(student)

    mem.sort()

    count = {}

    for student in mem:
        year = student[:2]
        faculty = student[2:4]

        if year not in count:
            count[year] = {}

        if faculty not in count[year]:
            count[year][faculty] = 1
        else:
            count[year][faculty] += 1

    for year in count:
        first = True

        for faculty in count[year]:
            if first:
                print(year, int(faculty), count[year][faculty])
                first = False
            else:
                print("--", int(faculty), count[year][faculty])
main()
