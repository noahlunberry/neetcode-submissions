#include <ranges>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        unordered_map<int, int> mp;

        //vector where each index represents the frequency
        vector<vector<int>> bucket(nums.size() + 1);

        for (const auto& num : nums) {
            mp[num]++;
        }

        for (auto& pair : mp){
            bucket[pair.second].push_back(pair.first);
        }
        
        vector<int> return_vector;

        size_t iter = k;

        for (const auto& i : bucket | std::views::reverse) {
            for (const auto& ip : i){
                return_vector.push_back(ip);
                iter--;
                if (return_vector.size() == k){return return_vector;}
            }
        }
        
        return return_vector;
    }
};
