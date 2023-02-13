n = int(input())
bush = [int(i) for i in input().split()]
bush_max = 0

for i in range(n):
    bush_sum = bush[i - 1] + bush[i] + bush[i + 1 if i < n - 1 else 0]
    if bush_sum > bush_max:
            bush_max = bush_sum

print(bush_max)