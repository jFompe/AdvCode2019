def check_increase(s):
    s2 = s.copy()
    s2.sort()
    return s == s2

def check_repeated(s):
    prev = s[0]
    for c in s[1:]:
        if prev == c:
            return True
        prev = c
    return False

def main ():
    start = 146810
    end = 612564

    total = 0

    for n in range(start, end+1):
        s = list(str(n))
        if (check_increase(s) and check_repeated(s)):
            total += 1
    print(total)



main()
