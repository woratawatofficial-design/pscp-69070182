"""DigitV3"""
def main():
    """This function gives you an output from txt to digits"""
    TOTAL = 0
    CURRENT = 0
    ONES = {
        'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,
        'six':6,'seven':7,'eight':8,'nine':9
    }
    TENS = {
        'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,
        'fifteen':15,'sixteen':16,'seventeen':17,
        'eighteen':18,'nineteen':19,'twenty':20,'thirty':30,'forty':40,
        'fifty':50,'sixty':60,'seventy':70,
        'eighty':80,'ninety':90
    }
    text = input().split()
    for word in text:
        if word in ONES:
            CURRENT += ONES[word]
        elif word in TENS:
            CURRENT += TENS[word]
        if word == 'hundred':
            CURRENT *= 100
        elif word == 'thousand':
            TOTAL += CURRENT*1000
            CURRENT = 0
    TOTAL += CURRENT
    print(TOTAL)
main()
