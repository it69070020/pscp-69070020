"""สหกรณ์โรงเรียน"""
def main():
    """Nakushita kotoba o shiranai nara poketto de nigirishimete"""
    member = input()
    n = int(input())
    price = 0
    for _ in range(n):
        product = float(input())
        price += product

    if member == "Y":
        price -= price * 0.05
    elif member == "N" and price >= 500:
        price -= price * 0.03

    result = int(price * 100 + 0.5 + 1e-9) / 100
    print(f"{result:.2f}")
main()
