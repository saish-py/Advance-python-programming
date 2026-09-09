def knapsack_bottom_up(weights, profits, capacity):

    n = len(weights)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):

        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:

                include = profits[i - 1] + dp[i - 1][w - weights[i - 1]]

                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:

                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def knapsack_top_down(weights, profits, n, capacity, memo):

    if n == 0 or capacity == 0:
        return 0

    if memo[n][capacity] != -1:

        return memo[n][capacity]

    if weights[n - 1] <= capacity:

        include = profits[n - 1] + knapsack_top_down(
            weights,
            profits,
            n - 1,
            capacity - weights[n - 1],
            memo
        )

        exclude = knapsack_top_down(
            weights,
            profits,
            n - 1,
            capacity,
            memo
        )

        memo[n][capacity] = max(include, exclude)

    else:

        memo[n][capacity] = knapsack_top_down(
            weights,
            profits,
            n - 1,
            capacity,
            memo
        )

    return memo[n][capacity]

# MAIN PROGRAM


weights = [2, 3, 4, 5]

profits = [3, 4, 5, 6]

capacity = 5

n = len(weights)


bottom_up_result = knapsack_bottom_up(weights, profits, capacity)

# Display the result
print("Maximum Profit using Bottom-Up:", bottom_up_result)


memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

top_down_result = knapsack_top_down(
    weights,
    profits,
    n,
    capacity,
    memo
)

# Display the result
print("Maximum Profit using Top-Down:", top_down_result)
