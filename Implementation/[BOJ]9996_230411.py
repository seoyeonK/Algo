import sys,re

N = int(sys.stdin.readline().strip())

pattern = sys.stdin.readline().strip()
pattern = '^'+pattern.replace("*",".*")+'$'
p = re.compile(pattern)


files = []
for i in range(N):
    files.append(sys.stdin.readline().strip())

for f in files : 
    m = p.match(f)
    if m:
        print("DA")
    else:
        print("NE")
#pattern = re.compile(rf"^{pattern}$"")