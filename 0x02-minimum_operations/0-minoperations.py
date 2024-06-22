#!/usr/bin/python3

def minOperations(n):
  """
  This function calculates the minimum number of operations needed to achieve
  exactly n 'H' characters in the file using only 'Copy All' and 'Paste' operations.

  Args:
      n: The target number of 'H' characters.

  Returns:
      The minimum number of operations required, or 0 if n is impossible.
  """

  # Base cases:
  if n == 0:
    return 0  # No operations needed for 0 characters
  elif n == 1:
    return 1  # 1 operation to copy the initial 'H'

  # Initialize an array to store minimum operations for all numbers up to n
  dp = [0] * (n + 1)

  # Fill the dp table using dynamic programming
  for i in range(2, n + 1):
    # Minimum operations for i characters is either:
    # 1. Copying the previous character (i-1) + 1 (paste)
    # 2. Pasting the previously copied characters (dp[i // 2]) if i is divisible by 2
    dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1) if i % 2 == 0 else dp[i - 1] + 1

  return dp[n]

# Example usage
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
