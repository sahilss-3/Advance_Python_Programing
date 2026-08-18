# Coin Change Problem
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter target amount: "))


dp = [float('inf')] * (amount + 1)
dp[0] = 0

for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[amount] == float('inf'):
    print("Amount cannot be made with given coins.")
else:
    print("Minimum number of coins:", dp[amount])

    '''
    Output

    Enter coin denominations: 1 6 8
    Enter target amount: 16
    Minimum number of coins: 2
    
    '''