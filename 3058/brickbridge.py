"""Imma build the bridge"""
def main():
    """Just use money lah"""
    a = int(input())
    b = int(input())
    goal = int(input())
    b_info = b * 5
    b_is_it_left = goal % 5
    if b_info + a < goal or b_is_it_left > a:
        print("-1")
    elif b_info > goal and not b_is_it_left:
        print(0)
    elif b_info < goal:
        print(goal - b_info)
    else:
        print(b_is_it_left)
main()
