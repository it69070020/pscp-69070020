"""yeah..frame...why u not just buy it?"""
def main():
    """Majiwaru sen to sen Kikazaru daisuki na Are kore sore"""
    sentences = []
    for _ in range(5):
        info = input()
        sentences.append(info)
    max_index = max(len(s) for s in sentences)
    width_space = max_index + 4

    print(width_space * "*")
    for s in sentences:
        print("* " + s.ljust(max_index) + " *")
    print(width_space * "*")
main()
