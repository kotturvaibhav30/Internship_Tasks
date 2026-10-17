import string

def print_rangoli(size):

    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        row = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append(row.center(4 * size - 3, '-'))

    print('\n'.join(lines[:0:-1] + lines))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
