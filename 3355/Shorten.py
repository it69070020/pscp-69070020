"""Just make it short...not so hard...nah im cooked"""
def main():
    """Saraba umarekawaru Amarini jinsei ga ui"""
    result = []
    info = int(input())
    start = info
    before_info = info
    while info != -1:
        info = int(input())
        if info - before_info > 1 or info == -1:
            if start == before_info:
                result.append(str(start))
            else:
                result.append(str(start) + "-" + str(before_info))
            start = info
        before_info = info
    print(", ".join(result))
main()
