
if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().split()))
    room_set = set(rooms)
    print((sum(room_set) * k - sum(rooms)) // (k - 1))

