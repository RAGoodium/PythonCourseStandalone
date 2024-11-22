numbers = [int(i) for i in input().split()]
n = int(input())
numbers.sort()
print(numbers[::n])