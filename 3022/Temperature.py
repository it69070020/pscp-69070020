"""Temperature"""
def main():
    """CHANGE BEFORE USE FUCK PEP8 JUST A FUCKING 1 VARIABLE WHY SO SERIOUS LAH WASTING MY TIME"""
    temp = float(input())
    temp_type = input()
    temp_type_change = input()
    result = temp
    if temp_type == "K" and temp_type_change == "C":
        result = temp - 273.15
    elif temp_type == "K" and temp_type_change == "F":
        result = (temp - 273.15) * 9 / 5 + 32
    elif temp_type == "K" and temp_type_change == "R":
        result = temp * 9 / 5
    elif temp_type == "C" and temp_type_change == "K":
        result = temp + 273.15
    elif temp_type == "C" and temp_type_change == "R":
        result = (temp + 273.15) * 9 / 5
    elif temp_type == "C" and temp_type_change == "F":
        result = temp * 9 / 5 + 32
    elif temp_type == "R" and temp_type_change == "C":
        result = temp * 5 / 9 - 273.15
    elif temp_type == "R" and temp_type_change == "K":
        result = temp * 5 / 9
    elif temp_type == "R" and temp_type_change == "F":
        result = temp - 459.67
    elif temp_type == "F" and temp_type_change == "K":
        result = (temp - 32) * 5 / 9 + 273.15
    elif temp_type == "F" and temp_type_change == "R":
        result = temp + 459.67
    elif temp_type == "F" and temp_type_change == "C":
        result = (temp - 32) * 5 / 9

    print(f"{result:.2f}")

main()
