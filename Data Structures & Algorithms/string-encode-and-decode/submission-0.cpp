#include <string>
using namespace std;
class Solution {
public:

    string encode(vector<string>& strs) {
        string str = "";
        for (string s : strs) {
            str.append(to_string(s.size()));

            str.push_back('#');
            str.append(s);
        }
        return str;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0; 
        while (i < s.size()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int length = stoi(s.substr(i, j - i));
            i = j + 1;
            j = i + length;
            res.push_back(s.substr(i, length));
            i = j;
        }
        return res;
    }
};
