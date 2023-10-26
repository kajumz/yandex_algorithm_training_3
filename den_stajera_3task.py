def find_longest_subsequence(n, b, A):
    dp = [1] * n

    for k in range(1, n+1):
        for j in range(1, k+1):
            if A[k-1] >= A[j-1] and A[k-1] - A[j-1] <= b:
                dp[k-1] = max(dp[k-1], dp[j-1] + 1)

    return int(max(dp) / 2)

n, b = map(int, input().split())
A = list(map(int, input().split()))

result = find_longest_subsequence(n, b, A)
print(result)
