"""Divine 10....why not 67"""
def main():
    """Kono yo de zouka yori kireina hana wa nai wa~"""
    number = int(input())
    new_number = number % 10
    number = number - new_number
    while number > 0:
        print(number, end=" ")
        number = number - 10
    print(0)
main()
