A, B, C = map(int, input().split())

sold = A // (C-B) + 1 if B < C else -1
print(sold)