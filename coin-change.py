def coinChange(coins, amount):
    # Initialize DP array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins to make amount 0

    # Fill the DP table
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the result
    return dp[amount] if dp[amount] != float('inf') else -1

# Example Usage
coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))  # Output: 3
