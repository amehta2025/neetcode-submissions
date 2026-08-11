class Solution {
public:
    bool isValid(string s) {
        map<char, char> m = {{')', '('}, {']', '['}, {'}', '{'}};
        stack<char> st;
        for (char c : s) {
            if (m.count(c)) { //if char is a closer
                if (st.empty() || st.top() != m[c]) {
                    return false;
                }
                else {
                    st.pop();
                }
            } else {
                st.push(c);
            }
        }
        return st.empty();
    }
};
