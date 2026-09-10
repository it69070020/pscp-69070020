"""frog JUMP AUTORISE"""
def main():
    """kimi wa watashi ni naremasenga Isshou jinrashiku Nai tari warattari shitete kudasai"""
    info = input()
    info_split = info.split()
    x = int(info_split[0])
    y = int(info_split[1])
    jump_left = y - x
    count = 1
    new_x = x
    while jump_left > 0:
        new_x -= 2
        if new_x <= 0:
            break
        jump_left -= new_x
        count += 1
    if jump_left <= 0:
        print(count)
    else:
        print(-1)
main()
