import re


def save_numbers():
    file = '../large.txt'
    with open(file, 'r') as f:
        line = map(int, f.readline().split())
        print(line)


def play_with_regex():
    string1 = 'he33llo 42 I\'m a 32 string -30 10.1'
    print(string1)
    re1 = r'\b\d+\b'
    re2 = r'[-]\b\d+\b'
    re4 = r'[-+]?\d*\.\d+|\d+'
    x = re.findall(r'[-+]?[0-9]*\.?[0-9]+', string1)
    generic_re = re.compile("(%s|%s|%s)" % (re1, re2, re4)).findall(string1)
    print(generic_re)


if __name__ == '__main__':
    save_numbers()
    play_with_regex()
