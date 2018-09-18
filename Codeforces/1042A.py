n = int(input())
m = int(input())
a = [int(input()) for i in range(n)]

s = sum(a)
mx = max(a)

res_min = max([mx, int((s+m+n-1)/n)])
res_max = mx + m

print(res_min, res_max)