"""FUBUKI HELLO NO WIFU I'M FRIEND HAHA"""
def main():
    """Ah Whip shita keeki no you na machi wa suki! yuki! maji Magic"""
    n = int(input())
    herd = {}
    for _ in range(n):
        parts = input().split('"')
        name = parts[1]
        code = parts[3]
        herd[name] = code

    if "Cat01" not in herd.values() and "Garfield" not in herd:
        herd["Garfield"] = "Cat01"
    if "Fox01" not in herd.values() and "Fubuki" not in herd:
        herd["Fubuki"] = "Fox01"

    cats = {}
    foxes = {}
    for item in herd.items():
        name = item[0]
        code = item[1]
        num = int(code[3:])
        if code.startswith("Cat"):
            cats[num] = name
        else:
            foxes[num] = name

    print("Cat :", len(cats))
    print("Fox :", len(foxes))
    for num in sorted(cats):
        print(cats[num], ":", herd[cats[num]])
    for num in sorted(foxes):
        print(foxes[num], ":", herd[foxes[num]])
main()
