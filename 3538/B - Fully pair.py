"""HAH U ALONE TAKE L LOSER"""
def main():
    """Watashi wa ame chikyuu o nazoru Hitotsubu de wa kizuku koto no nai ame"""
    text = input()
    waiting_line = ""
    for char in text:
        if char in waiting_line:
            waiting_line = waiting_line.replace(char, "")
        else:
            waiting_line = waiting_line + char
    answer = ""
    for char in text:
        if char in waiting_line and char not in answer:
            answer = answer + char
    if not waiting_line:
        print("fully paired")
    else:
        print(answer)
main()
