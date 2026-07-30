"""OMG SURPRISING"""
def main():
    """IM SHOCKED AHHHH"""
    total = float(input())
    highest = float(input())
    lowest = total - (2*highest)
    if lowest < 0:
        lowest = 0
    final = highest - lowest
    if 0 <= final <= 2 :
        print("Not surprising")
    else:
        print("Surprising")
main()
