"""AEIOU BUT PRO MAX"""
def main():
    """WHY IS HE GOONING?"""
    text = input()
    text_lower = text.lower()
    vowels = "aeiou"
    all_letter = [0] * 5

    for ch in text_lower:
        if ch in vowels:
            index = vowels.index(ch)
            all_letter[index] = all_letter[index] + 1

    for i  in range(5):
        if all_letter[i] > 0:
            print(vowels[i] + " : " + str(all_letter[i]))

main()
