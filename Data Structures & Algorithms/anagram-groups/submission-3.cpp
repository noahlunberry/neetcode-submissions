#include <algorithm>
#include <string>


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        
        for (const auto& word : strs) {
            std::string newString = word;
            std::sort(newString.begin(), newString.end());
            mp[newString].push_back(word);        
        }
        
        vector<vector<string>> result;

        for ( auto& pair : mp ) {
            result.push_back(pair.second);
        }
        return result;
    }
};
