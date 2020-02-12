"""

Find the first longest consecutive char
Venky, 05/10/18

"""


def find_longest_cons_char(s):
    # Find string length
    l = len(s)
    c = s[0]
    # Char length
    n = 1
    # Current long char
    c_now = c
    # Current long length
    nc = 0

    for i in range(1, l):
        if s[i] == c:
            n += 1
        else:
            if n > nc:
                c_now, nc = c, n
            c, n = s[i], 1
        if n > nc:
            c_now, nc = c, n
    return c_now, nc


"""

Find all the longest consecutive characters

"""


def find_longest_cons_chars(s):
    # Find string length
    l = len(s)
    c = s[0]
    # Char length
    n = 1
    # Current long char
    c_now = []
    # Current long length
    nc = 0

    for i in range(1, l):
        if s[i] == c:
            n += 1
        else:
            if n == nc:
                c_now.append(c)
                nc = n
            if n > nc:
                c_now, nc = [c,], n
            c, n = s[i], 1
    if n > nc:
        c_now, nc = [c], n
    # Skip dup char
    if n == nc and c not in c_now:
        c_now.append(c)
    return c_now, nc


if __name__ == "__main__":
    # Test for for longest char
    c, n = find_longest_cons_char("AAABBCCJJJKKKKKLLLLMNMMMZZZZZZ")
    print("Char = {}  Length = {}".format(c, n))
    c, n = find_longest_cons_char("AAABBCCJJJKKKKKLLLLMNMMM")
    print("Char = {}  Length = {}".format(c, n))
    c, n = find_longest_cons_char("AAABBCCJJJJKKKLLLLMNMMM")
    print("Char = {}  Length = {}".format(c, n))

    # Test for for all longest char(s)
    c, n = find_longest_cons_chars("AAABBCCJJJKKKKKLLLLMNMMM")
    print("Char = {}  Length = {}".format(c, n))
    c, n = find_longest_cons_chars("AAABBCCJJJJKKKLLLLMNMMM")
    print("Char = {}  Length = {}".format(c, n))
    c, n = find_longest_cons_chars("AAAAAABBCCJJJZZZZZZKKKKKLLLLMNMMMZZZZZZ")
    print("Char = {}  Length = {}".format(c, n))
    c, n = find_longest_cons_chars("AAAAABBCCJJJKKKKKLLLLMNMMMZZZZZZ")
    print("Char = {}  Length = {}".format(c, n))
