numbers = [int(i) for i in input().split()]
n = int(input())
print(sum(numbers[-n:]))