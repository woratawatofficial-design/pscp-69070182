"""ตรวจตัวอักษร"""
Text = input()
if len(Text) == 5:
    Text = Text.lower() [::-1]
print(Text)
