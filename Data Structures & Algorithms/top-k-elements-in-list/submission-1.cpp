#include <map>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> m;
        for (int i = 0; i < nums.size(); ++i) {
            m[nums[i]]++;
        }
        vector<pair<int, int>> m2;
        for (const auto& p : m) {
            m2.push_back({p.second, p.first});
        }
        vector<int> sol;
        sort(m2.rbegin(), m2.rend());
        for (int i = 0; i < k; ++i) {
            sol.push_back(m2[i].second);
        }
        return sol;
    }
};
