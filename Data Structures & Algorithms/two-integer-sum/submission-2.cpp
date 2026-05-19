class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> mp;
        
        int i = 0;
        for (const auto& num : nums) {
            int needed = target - num;
            if (mp.count(needed)) {
                return{mp[needed], i};
            }
            mp[num] = i;
            i++;
        }
    }
};
