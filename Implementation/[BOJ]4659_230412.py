# 모음 최소 1개 - a e i o u
# 모음/자음 연속 3개 X
# 같은 글자 연속 두번 x - 예외) ee, oo
import re
while 1:
    s=input()
    if s=='end':break
    case1 = len(re.findall('[aeiou]',s)) != 0
    case2 = len(re.findall('[aeiou]{3}|[^aeiou]{3}',s))==0
    case3 = len(re.findall('([a-df-np-z])\\1',s))==0
    if case1 and case2 and case3:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')


