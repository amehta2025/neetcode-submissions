#include <unordered_set>
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for (int i : nums) {
            s.insert(i);
        }
        return s.size() != nums.size();
    }
};