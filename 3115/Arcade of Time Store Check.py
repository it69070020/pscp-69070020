"""Arcade of Time: Store Check"""
def main():
    """	rurukaririkarura rirarurara kirai ni naranaide"""
    info = input()
    info_splited = info.split()
    num = int(info_splited[0])

    stores = []

    for _ in range(num):
        store_info = input().split()
        start = int(store_info[0])
        stop = int(store_info[1])
        stores.append((start, stop))

    check_times = input().split()
    check_times = [int(k) for k in check_times]

    result = []
    for k in check_times:
        count = 0
        for start, stop in stores:
            if start <= k < stop:
                count += 1
        result.append(str(count))
    print(" ".join(result))
main()
