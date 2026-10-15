
import re

N = int(input())

for _ in range(N):
    phone = input()
    if re.fullmatch(r'[789]\d{9}', phone):
        print("YES")
    else:
        print("NO")

