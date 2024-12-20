n = input().split()
ans = []
for i in n:
    if len(i) > 1:
        k = i[0] + i[-1]
        ans.append(k)
    else:
        ans.append(i)
print(f'Результат:', *ans)