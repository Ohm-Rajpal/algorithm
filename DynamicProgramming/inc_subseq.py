# largest increasing subsequence
def longest_subseq(arr):
    dp = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(0, i):
            if arr[j] > arr[i]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)

def main():
    arr = [5, 2, 8, 6]
    print(longest_subseq(arr))

if __name__ == "__main__":
    main()