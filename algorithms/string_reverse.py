"""
REVERSE A STRING - One char at a time using recursion
Venky, 02/26/2017

"""


def reverse_str1(s):
    if s == "":
        return s
    return s[-1] + reverse_str1(s[0 : len(s) - 1])


"""
Using python list feature. 
"""


def reverse_str2(s):
    return s[::-1]


"""
Using for..loop
"""


def reverse_str3(s):
    rs = ""
    for i in range(len(s) - 1, -1, -1):
        rs = rs + s[i]
    return rs


if __name__ == "__main__":

    print(reverse_str1("ABCDEFGH"))
    print(reverse_str2("ABCDEFGH"))
    print(reverse_str3("ABCDEFGH"))
