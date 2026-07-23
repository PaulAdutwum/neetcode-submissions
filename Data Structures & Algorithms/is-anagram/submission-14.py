class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = {}
        if len(s) != len(t):
            return False 


        for sc in s:
            freq_map[sc] = freq_map.get(sc, 0) + 1

        for tc in t:
            freq_map[tc] = freq_map.get(tc, 0) - 1

        for count in freq_map.values():
            if count != 0:
                return False 

        return True 

        