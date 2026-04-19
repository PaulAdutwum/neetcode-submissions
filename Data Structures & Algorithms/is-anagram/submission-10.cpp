class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){
            return false;
        }
        unordered_map<char, int> freq;

        for (char ch : s){
            freq[ch] += 1;

        }

        for(char ch: t){
            freq[ch] -= 1;
            if (freq[ch] < 0){
                return false;
            }
        } 
        return true;

        
    }
};
