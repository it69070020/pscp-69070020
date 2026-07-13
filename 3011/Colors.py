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
    elif first_color == "Red" and second_color == "Red":
        print("Red")
    elif first_color == "Yellow" and second_color == "Yellow":
        print("Yellow")
    elif first_color == "Blue" and second_color == "Blue":
        print("Blue")
    else:
        print("Error")

main()
