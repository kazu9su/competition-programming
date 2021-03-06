n = 3
m = 3
a = [1, 2, 3]
M = 10000

dp = [[0] * (m+1) for i in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

for i in range(n):
    for j in range(1, m+1):
        if j - a[i] - 1 >= 0:
            dp[i+1][j] = dp[i+1][j-1] + dp[i][j] - dp[i][j - a[i] - 1]
        else:
            dp[i+1][j] = dp[i+1][j-1] + dp[i][j]

print(dp[n][m])
