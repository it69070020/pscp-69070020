"""I want You, Want You, IQ ga sagatte iku kanji"""
def main():
    """kamippoi na sore hikyou kamippoi na sore"""
    info = input()
    info_splited = info.split()
    start = str(info_splited[0])
    end = str(info_splited[1])
    weight = float(input())
    BKK_TO_CNX = 10 + (weight * 30)
    CNX_TO_UBP = 15 + (weight * 40)
    UBP_TO_BKK = 20 + (weight * 40)
    BKK_TO_PKT = 25 + (weight * 50)
    PKT_TO_CNX = 30 + (weight * 60)
    UBP_TO_PKT = 40 + (weight * 70)
    if start == "BKK" and end == "CNX":
        print(f"{BKK_TO_CNX:.2f}")
    elif start == "CNX" and end == "UBP":
        print(f"{CNX_TO_UBP:.2f}")
    elif start == "UBP" and end == "BKK":
        print(f"{UBP_TO_BKK:.2f}")
    elif start == "BKK" and end == "PKT":
        print(f"{BKK_TO_PKT:.2f}")
    elif start == "PKT" and end == "CNX":
        print(f"{PKT_TO_CNX:.2f}")
    elif start == "UBP" and end == "PKT":
        print(f"{UBP_TO_PKT:.2f}")
    else:
        print("Error")
main()
