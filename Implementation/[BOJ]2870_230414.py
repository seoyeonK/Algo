#다른 사람 풀이

import re
answer = []
for _ in range(int(input())):
    numbers = re.findall('\d+',input()) #숫자만 필터링해서 리스트로 바꿈
    answer.extend(list(map(int, numbers))) #map으로 int형변환 (0지우려고)
print('\n'.join(map(str, sorted(answer)))) #오름차순 출력


expression = re.split('',)