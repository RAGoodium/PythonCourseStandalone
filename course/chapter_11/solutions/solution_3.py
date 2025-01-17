numbers = input().split()
target = int(input())
done = 0
for n in numbers:
    n = int(n)
    minus = target - n
    answer = (n, minus)
    if str(minus) in numbers:
        print(answer)
        done +=1
        break
if done == 0:
    print(target)
    
