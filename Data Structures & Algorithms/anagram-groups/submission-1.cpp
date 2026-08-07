#include <vector>
#include <map>
#include <unordered_set>
#include <string>
using namespace std;
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> r;
        for (const auto& a : strs) {
            string sortthis = a;
            sort(sortthis.begin(), sortthis.end());
            r[sortthis].push_back(a);
        }
        vector<vector<string>> result;
        for (auto& pair : r) {
            result.push_back(pair.second);
        }
        return result;
    }
};
