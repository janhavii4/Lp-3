n = 4
capacity = 5

weight = [2, 3, 4, 5]
value = [3, 4, 5, 6]

# Create DP table
dp = [[0 for j in range(capacity + 1)]
      for i in range(n + 1)]

# Fill the table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weight[i - 1] <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                value[i - 1] + dp[i - 1][w - weight[i - 1]]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Display DP table
print("DP Table:")
for row in dp:
    print(row)

# Find selected items
w = capacity
selected = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected.append(i)
        w -= weight[i - 1]

print("\nSelected items:", selected[::-1])
print("Maximum value:", dp[n][capacity])