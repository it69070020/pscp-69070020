"""Colors"""
def main():
    """Primary color"""

    first_color = input().strip()
    second_color = input().strip()
    new_first_color = first_color.capitalize()
    new_second_color = second_color.capitalize()

    if new_first_color == "Red" and new_second_color == "Yellow":
        print("Orange")
    elif new_first_color == "Red" and new_second_color == "Blue":
        print("Violet")
    elif new_first_color == "Yellow" and new_second_color == "Blue":
        print("Green")
    elif new_first_color == "Red" and new_second_color == "Red":
        print("Red")
    elif new_first_color == "Yellow" and new_second_color == "Yellow":
        print("Yellow")
    elif new_first_color == "Blue" and new_second_color == "Blue":
        print("Blue")
    else:
        print("Error")

main()
