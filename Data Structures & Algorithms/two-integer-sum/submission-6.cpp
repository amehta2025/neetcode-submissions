#include <map>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m;
        vector<int> v;
        for (int i = 0; i < nums.size(); ++i) {
            m[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); ++i) {
            int difference = target - nums[i];
            if (m.count(difference) && m[difference] != i) {
                v = {i, m[difference]};
                break;
            }
        }
        return v;
    }
};
