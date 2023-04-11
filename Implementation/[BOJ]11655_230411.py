# S = input()
# answer = ""
# for s in S:
#     if 'a' <= s and s <= 'z':
#         s_ = ord(s) + 13
#         if s_ > 122:
#             s_ -= 26    
#         answer+=chr(s_)
#     elif 'A' <= s and s <= 'Z':
#         s_ = ord(s) + 13
#         if s_ > 90 :
#             s_ -= 26
#         answer+=chr(s_)
#     else:
#         answer+=s

# print(answer)

a = list(input())
for i in range(len(a)):
    if a[i].isupper(): a[i] = chr(65+(ord(a[i])-65+13)%26)
    if a[i].islower(): a[i] = chr(97+(ord(a[i])-97+13)%26)
print(''.join(a))