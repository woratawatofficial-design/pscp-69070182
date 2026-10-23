"""Histogram"""
def main():
    """This is histogram func"""
    HISTOGRAM = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    HAVE = []
    COUNT = 0
    text = input()
    for i in text:
        if i in HISTOGRAM:
            HAVE.append(i)
    for j in HISTOGRAM:
        if j in HAVE:
            BAR = ''
            COUNT = HAVE.count(j)
            while COUNT > 5:
                BAR += "-----|"
                COUNT -= 5
            BAR += COUNT*'-'
            print(f"{j} : {BAR}")
main()
