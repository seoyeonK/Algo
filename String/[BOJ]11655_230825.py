S = input().rstrip()
rot = ''

for s in S:
    if s.isalpha():
        ns = ord(s) + 13
        if (s.islower() and ns > 122) or (s.isupper() and ns > 90):
            ns -= 26
        s = chr(ns)
    rot += s
print(rot)