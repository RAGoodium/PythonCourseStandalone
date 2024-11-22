numbers = [int(i) for i in input().split()]
n = int(input())

print(f'Максимум: {max(numbers[n:-n])}')
print(f'Минимум: {min(numbers[n:-n])}')