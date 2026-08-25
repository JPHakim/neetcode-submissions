class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_c = defaultdict(int)
        s2_c = defaultdict(int)
        start = 0

        for char in s1:
            s1_c[char] += 1
        for end in range(len(s2)):
            s2_c[s2[end]] += 1
            if end - start + 1 == len(s1):
                if s2_c == s1_c:
                    return True
                if s2_c[s2[start]] > 1:
                   s2_c[s2[start]] -= 1 
                else:
                    s2_c.pop(s2[start],None)
                start+=1
        return False
            


        