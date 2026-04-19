from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        This problem requires us to find and check if two given strigns
        are anagrams. 

        What is an anagram?
        An angram are words that contains the same letters, such that every letter
        in one of the words appears in the other word.  


        This pblem can be approahced form a classic two pointe techniue from multioplle
        words. This will allow us ot solve this prblem with a time comlexioty of O(N) 



        approach: 
         i = 0 
         first check if both words have the same lenth. 

         If length are the not the same, we can quickly return false. 

         while i =< len(s)
         if s[i] in t:
            return True 
        """
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)





        