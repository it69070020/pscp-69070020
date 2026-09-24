"""ICE ELATION"""
def main():
    """Nee atashi shitteru yo kimi ga hitori "****" shiteru no shitteru yo"""
    first_color = input().split()
    second_color = input().split()
    Red1 = int(first_color[0])
    Red2 = int(second_color[0])
    Green1 = int(first_color[1])
    Green2 = int(second_color[1])
    Blue1 = int(first_color[2])
    Blue2 = int(second_color[2])
    Red_final = (Red1 + Red2) // 2
    Green_final = (Green1 + Green2) // 2
    Blue_final = (Blue1 + Blue2) // 2
    print(f"{Red_final} {Green_final} {Blue_final}")
main()
