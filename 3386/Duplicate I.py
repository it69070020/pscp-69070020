"""DID IMPOSTER IN OUR BASE???"""
def main():
    """Reini reini motomeru mono dake kaita Kokoro shimatte matte! Hontoha sakebitai no yo"""
    first = int(input())
    second = int(input())
    first_info = []
    second_info = []
    for _ in range(first):
        first_info.append(input())
    for _ in range(second):
        second_info.append(input())
    both = sorted(set(first_info) & set(second_info), reverse=True)
    if both:
        print("\n".join(both))
    else:
        print("Nope")
main()
