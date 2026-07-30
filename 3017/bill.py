"""Bill for fud"""
def main():
    """I ordered b'or'of'wo'er"""
    money = int(input())
    additional_money = money * 0.10
    after_plus = money + additional_money
    final_money = after_plus * 1.07
    below_fifteen = (money + 50) * 1.07
    more_than_thouson = (money + 1000) * 1.07

    if  50 <= additional_money <= 1000:
        print(f"{final_money:.2f}")
    elif 50 > additional_money:
        print(f"{below_fifteen:.2f}")
    else:
        print(f"{more_than_thouson:.2f}")
main()
