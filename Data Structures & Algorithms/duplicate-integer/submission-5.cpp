class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> mySet;

        for (const auto& num : nums) {
            std::cout<< num << std::endl;
            if (mySet.contains(num)) {return true;}
            mySet.insert(num);
        }

        return false;
    }
};