"""MyBrainTrembles"""
def main():
    """Find the number of students who received the message"""
    N, S = map(int, input().split())
    students = []
    for _ in range(N):
        students.append(int(input()))
    found = [S]
    current = S
    while True:
        next_student = students[current - 1]
        if not next_student:
            break
        if next_student in found:
            break
        found.append(next_student)
        current = next_student
    print(len(found))
main()
