"""Arrow Solution"""
def draw_arrow(direction_type, n):
    """ฟังก์ชันสำหรับวาดลูกธนู 1 ดอก"""
    if direction_type == 'R':
        # ครึ่งบนรวมแถวกลาง
        for i in range(n):
            print(' ' * i + '*' * (n - i))
        # ครึ่งล่าง
        for i in range(n - 2, -1, -1):
            print(' ' * i + '*' * (n - i))

    elif direction_type == 'L':
        # ครึ่งบนรวมแถวกลาง
        for i in range(n - 1, -1, -1):
            print(' ' * i + '*' * (n - (n - 1 - i)))
        # ครึ่งล่าง
        for i in range(1, n):
            print(' ' * i + '*' * (n - i))

def main():
    """Main Function"""
    direction = input().upper()
    n = int(input())

    for idx, char in enumerate(direction):
        if idx > 0:
            print()  # เว้นบรรทัดคั่นระหว่างลูกธนูแต่ละดอก
        draw_arrow(char, n)

main()