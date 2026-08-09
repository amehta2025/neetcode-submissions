#include <stack>
#include <unordered_map>
using namespace std;
class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> pairs = {{'}', '{'},{']', '['}, {')', '('}};
        stack<char> st;
        for (char c : s) {
            if (pairs.count(c)) {
                if (st.empty() || pairs[c] != st.top()) {
                    return false;
    
                }
                st.pop();
            } else {
                st.push(c);
            }
        }
        return st.empty();
    }
};
