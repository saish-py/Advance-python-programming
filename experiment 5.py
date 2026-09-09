def find_lcs(X, Y):

    m = len(X)

    n = len(Y)


    dp=[[0 for j in range(n+1)] for i in range(m + 1)]

    for i in range(1, m+1):

        for j in range(1, n + 1):

            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1


            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs_length = dp[m][n]

    lcs = ""

    i = m
    j = n

    while i > 0 and j > 0:

        if X[i - 1] == Y[j-1]:

            lcs = X[i-1] + lcs

            i = i-1
            j = j-1

        elif dp[i-1][j] > dp[i][j-1]:
            i = i-1

        else:
            j = j-1

    return lcs, lcs_length


X = input("Enter first sequence: ")

Y = input("Enter second sequence: ")

lcs, length = find_lcs(X, Y)

print("Longest Common Subsequence:", lcs)

print("Length of LCS:", length)
