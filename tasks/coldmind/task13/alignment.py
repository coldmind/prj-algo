# coding=utf-8

def _match_score(a, b):
    return 0 if a == b else 1


def align_str(s1, s2, damerau_levenshtein=False):
    """
    Wagner–Fischer algorithm is used
    for the alignment.
    """
    m, n = len(s1), len(s2)
    costs = [
        [0 for x in xrange(0, n + 1)]
        for y in xrange(0, m + 1)
    ]
    for i in xrange(0, m + 1):
        costs[i][0] = i
    for j in xrange(0, n + 1):
        costs[0][j] = j
    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            costs[i][j] = min([
                costs[i - 1][j - 1] + _match_score(s1[i - 1], s2[j - 1]),  # Substitution
                costs[i][j - 1] + 1,                                       # Insertion
                costs[i - 1][j] + 1,                                       # Deletion
            ])
            if damerau_levenshtein:
                if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                    costs[i][j] = min([costs[i][j], costs[i - 2][j - 2] + 1])
    aligned_s1 = ""
    aligned_s2 = ""
    while m > 0 or n > 0:
        # Match
        if m > 0 and n > 0 and costs[m][n] == (costs[m - 1][n - 1] + _match_score(s1[m - 1], s2[n - 1])):
            aligned_s1 += s1[m - 1]
            aligned_s2 += s2[n - 1]
            m -= 1
            n -= 1
        # Insert
        elif m > 0 and costs[m][n] == (costs[m - 1][n] + 1):
            aligned_s1 += s1[m - 1]
            aligned_s2 += "-"
            m -= 1
        # Delete
        else:
            aligned_s1 += "-"
            aligned_s2 += s2[n - 1]
            n -= 1
    print aligned_s1[::-1]
    print aligned_s2[::-1]
    print "\n"


align_str("sunday", "saturday")
align_str("AGTACGCA", "TATGC")
align_str("FTFTALILLAVAV", "FTALLLAAV")

align_str("animals", "ainmals")
align_str("animals", "ainmals", damerau_levenshtein=True)
