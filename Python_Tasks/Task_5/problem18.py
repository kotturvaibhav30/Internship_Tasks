def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    n = len(string)

    for i in range(n):
        points = n - i

        if string[i] in vowels:
            kevin += points
        else:
            stuart += points

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
