class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> mp;
        for (const auto& letter : s) {
            mp[letter]++;
        }
        for (const auto& letter : t) {
            mp[letter]--;
        }
        for (auto& [key, val] :  mp) {
            if (val != 0) {
                return  false;
            }
        }
        return true;
    }
};
