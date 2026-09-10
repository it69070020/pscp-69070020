"""I BELIVE IN A HEART OF A CARD"""
def main():
    """Hikikomori zettai jasutisu Ore no watashi dake no ori no naka de"""
    card = input().upper()
    if card[0] in "23456789" or "10" in card:
        if "D" in card:
            if "10" in card:
                print(card[0:2]+" of diamonds")
            else:
                print(card[0]+" of diamonds")
        elif "H" in card:
            if "10" in card:
                print(card[0:2]+" of hearts")
            else:
                print(card[0]+" of hearts")
        elif "S" in card:
            if "10" in card:
                print(card[0:2]+" of spades")
            else:
                print(card[0]+" of spades")
        elif "C" in card:
            if "10" in card:
                print(card[0:2]+" of clubs")
            else:
                print(card[0]+" of clubs")
    else:
        if card == "JD":
            print("jack of diamonds")
        elif card == "JH":
            print("jack of hearts")
        elif card == "JS":
            print("jack of spades")
        elif card == "JC":
            print("jack of clubs")
        elif card == "AD":
            print("ace of diamonds")
        elif card == "AH":
            print("ace of hearts")
        elif card == "AS":
            print("ace of spades")
        elif card == "AC":
            print("ace of clubs")
        elif card == "QD":
            print("queen of diamonds")
        elif card == "QH":
            print("queen of hearts")
        elif card == "QS":
            print("queen of spades")
        elif card == "QC":
            print("queen of clubs")
        elif card == "KD":
            print("king of diamonds")
        elif card == "KH":
            print("king of hearts")
        elif card == "KS":
            print("king of spades")
        elif card == "KC":
            print("king of clubs")
main()
