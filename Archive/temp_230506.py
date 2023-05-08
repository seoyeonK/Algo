def GCF(x,y):
    while y:
        x, y = y, x%y
    return x

def GCM(x,y):
    return (x*y)//GCF(x,y)
print(GCF(12,30))
print(GCM(12,30))