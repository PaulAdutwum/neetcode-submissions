class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Input:
            ** string s 
            ** integer k

        Outuput:
            ** the lenght of longest susbtring which cont
            ains single character 


        Goal: 

            ** return output: 

        Apprach:

        Notice that this is sliding window problem

        -- use a left and right pointers as windows endpoints

        -- we use a hashmap to help me kekp track of the 
        current count of elments in the widnow so far 

            MOST IMPOTANT CONFUSION EARLIER
                I was confused whether i had only replace 
                chars in the entire string and return the longes
                susbtring taht cocntains only one char 


                But it turns out the that will not solve the problem
                the acutal prolems wants to find the longest continous 
                substring that tht will give s one disitint elelment

                This means we havaen slid ouw windown and return the 
                the lengh and find the the max freq of char in the window
                the check if this thje number of reperlcement needed is less than 
                k. 

                Formula: 

                Given a partiucaular owidndow, we wnat sing the 
                  repalcement neede = lenth of current window - the max_freq of lements 

                  lenght = right - left + 1 
                  max_freq = max(elemtnes we will stor in the hashnmap)

                  our hashmap will help keep track of the coutns fo elements 
        """

        count = {}
        left = 0 
        res = 0 
        max_freq = 0

        for right in range(len(s)):
            # add current element to the the count map
            count[s[right]] = count.get(s[right], 0) + 1

            #  no e find the max_freq element in counts

            max_freq = max(max_freq, count[s[right]])

            # now with max freq we had to find replacenemnt need

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1 
                left += 1 

            res = max(res, right - left + 1)


        return res





        