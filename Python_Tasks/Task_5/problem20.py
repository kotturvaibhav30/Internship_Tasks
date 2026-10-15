
from collections import deque

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        cubes = deque(map(int, input().split()))
        last = float('inf')
        possible = True

        while cubes:
            if cubes[0] >= cubes[-1]:
                cube = cubes.popleft()
            else:
                cube = cubes.pop()

            if cube > last:
                possible = False
                break

            last = cube

        print("Yes" if possible else "No")

