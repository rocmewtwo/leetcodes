# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from typing import List
from collections import Counter

def longestPalindrome(words: List[str]) -> int:
    # create hash table
    words_table = Counter(words)

    lonely_palindromes = 0
    ans = 0
    for s in words_table:
        # skip counter 0
        if words_table[s] <= 0:
            continue

        ## self palindrome
        if (s[0] == s[1]):
            ans += int(words_table[s] / 2) * 4
            lonely_palindromes += int(words_table[s] % 2)
            continue

        ## check pair
        pair_key = f'{s[1]}{s[0]}'
        if (words_table[pair_key] > 0):
            ans += 4 * min(words_table[pair_key], words_table[s])
            # mark pair used
            words_table[pair_key] = 0

    ## append self palindrome
    if (lonely_palindromes):
        ans += 2

    return ans

if __name__ == "__main__":
    words = ["lc","cl","gg"] # 6
    words = ["ab","ty","yt","lc","cl","ab"] # 8
    words = ["cc","ll","xx"] # 2
    words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"] # 22
    print(longestPalindrome(words))