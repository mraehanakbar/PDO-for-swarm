import math

def funct(x1,x2):
    i = 1
    max1 = 0
    max2 = 0
    while i <= 5:
        n = -1
        k = n * i
        result1 = (k * math.cos(k + 1 * x1 + 1))
        if result1 > max1:
            max1 = result1
        print("\n")
        result2 = (i * math.cos(i + 1 * x2 + 1))
        if result2 > max2:
            max2 = result2
        i += 1
    print("max x1 dengan nilai", x1 ," :" ,max1)
    print("max x2 dengan nilai", x2 ," :" ,max2)

hitung1 = -40
hitung2 = -40

while hitung1 < 50:
    funct(hitung1,hitung2)
    hitung1 += 10
    hitung2 += 10
