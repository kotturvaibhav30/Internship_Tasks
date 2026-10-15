
if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))

    x = 0x345678
    mult = 1000003
    length = len(t)
    mask = (1 << 64) - 1

    for item in t:
        x = ((x ^ hash(item)) * mult) & mask
        length -= 1
        mult = (mult + 82520 + length + length) & mask

    x = (x + 97531) & mask

    if x >= (1 << 63):
        x -= (1 << 64)

    print(x)

