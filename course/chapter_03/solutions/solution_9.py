n = int(input())
d = 10
numb = 0
summ = 0
while numb >= 0:
    numb = n % d
    d = d * 10
    summ = summ + numb
print(summ)