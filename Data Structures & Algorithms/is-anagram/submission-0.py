class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ht_1 = defaultdict(int)
        ht_2 = defaultdict(int)

        for char in s:
            ht_1[char] += 1
        for char in t:
            ht_2[char] += 1
        return ht_1 == ht_2
        