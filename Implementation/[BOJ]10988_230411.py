#
word = input()

if word == word[::-1]:
    print(1)
else:
    print(0)

# 30616KB, 32ms
word = list(word)
word_reverse = list(reversed(word))