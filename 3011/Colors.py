"""Colors"""
def main():
    """Primary color"""

    first_color = str(input())
    second_color = str(input())

    if first_color == "Red" and second_color == "Yellow":
        print("Orange")
    elif first_color == "Red" and second_color == "Blue":
        print("Violet")
    elif first_color == "Yellow" and second_color == "Blue":
        print("Green")
    else:
        print("Error")

main()
