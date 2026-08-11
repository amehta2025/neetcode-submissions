#include <map>
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> one;
        map<char, int> two;
        if (s.size() != t.size()) return false;

        for (int i = 0; i < s.size(); ++i) {
            one[s[i]]++;
            two[t[i]]++;
        }
        return one == two;
    }
};
