class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        int middle;
        while (l <= r) { //<= because consider the case where you have 1 element
            middle = (l + r) / 2;
            if (target > nums[middle]) {
                l = middle + 1;
            }
            else if (target < nums[middle]) {
                r = middle - 1;   //to shrink the range
            }
            else {
                return middle;
            }
        }
        return -1;
    }
};
