#include <vector>
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for (int i = 0; i < matrix.size(); ++i) {
            int l = 0;
            int r = matrix[i].size() - 1;
            int medium;
            while (l <= r) {
                medium = (l + r) /2;
                if (target > matrix[i][medium]) {
                    l = medium + 1;
                }
                else if (target < matrix[i][medium]) {
                    r = medium - 1;
                }
                else {
                    return true;
                }
            }
        }
        return false;
    }
};
