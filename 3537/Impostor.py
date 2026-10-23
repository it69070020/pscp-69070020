"""IMPASTA SUSSY BAKA TUHG TUNG SAHUR AMOGUS OHIO SUSMAXXING :CRY:"""
import json
def main():
    """Demo, hontou wa, hontou wa, hontou wa, hontou ni samui nda"""
    amogus = {}
    while True:
        info = input()
        if info == "Start":
            break
        amogus.update(json.loads(info))
    full = amogus.copy()
    die = input()
    while die != "End":
        amogus.pop(die)
        die = input()
    print(list(amogus.values()).count("Impostor"), "Impostor Remains")
    print("***Alive***")
    for i in sorted(amogus):
        print(i, ":", amogus[i])
    print("***Dead***")
    for i in sorted(full):
        if i not in amogus:
            print(i, ":", full[i])
main()
