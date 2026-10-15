# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    m = int(input())
    set_a = set(map(int, input().split()))
    n = int(input())
    set_b = set(map(int, input().split()))

    result = sorted(set_a.symmetric_difference(set_b))

    for num in result:
        print(num)

