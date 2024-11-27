numbers = [int(i) for i in input().split()]
n = int(input())
print(sorted(numbers[::n]))