"""Lottery! yay i lost...FAH"""
def main():
    """Saa, an'yo an’yo kocchi oide Te wo tataite aruke rattatta"""
    prize = input()
    bought = input()
    prize_split = prize.split()
    bought_split = bought.split()
    prize_letter = str(prize_split[0])
    prize_num = str(prize_split[1])
    bought_letter = str(bought_split[0])
    bought_num = str(bought_split[1])
    if prize_letter == bought_letter and prize_num == bought_num:
        print("1000000")
    elif prize_letter != bought_letter and prize_num == bought_num:
        print("100000")
    elif prize_letter == bought_letter and prize_num[2:5] == bought_num[2:5]:
        print("2000")
    elif prize_letter == bought_letter and prize_num[3:5] == bought_num[3:5]:
        print("1000")
    elif prize_letter != bought_letter and prize_num[2:5] == bought_num[2:5]:
        print("200")
    elif prize_letter != bought_letter and prize_num[3:5] == bought_num[3:5]:
        print("100")
    elif prize_letter == bought_letter and prize_num != bought_num:
        print("20")
    else:
        print("0")
main()
