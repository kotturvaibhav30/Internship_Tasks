
A = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    other = set(map(int, input().split()))
    if not A.issuperset(other) or A == other:
        result = False
        break

print(result)

