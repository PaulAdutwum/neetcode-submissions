class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encode = ""
        for s in strs:
            encode += str(len(s)) + "#" + s
        return encode

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []
        while i < len(s):
            j = i 

            while j < len(s) and s[j] != "#":
                j += 1

            length = int(s[i : j])

            word = s[j+1 : j+1 + length]

            res.append(word)

            i = j+1 + length

        return res 



    
