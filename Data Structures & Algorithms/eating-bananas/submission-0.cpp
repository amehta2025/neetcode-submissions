#include <vector>
using namespace std;
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());

        int ans = r;
        int middle;
        while (l <= r) {
             middle = l + (r - l) / 2;   //constraint version of middle = (l + r) /2
             long long totaltime = 0;
            for (int p : piles) {
                totaltime += (p + middle - 1) / middle; //essentially the same way of doing ceil(static_cast<double> p/m)
            }
            if (totaltime <= h) {
                ans = middle; //as slower speed, hours increase. setting ans = middle here guarantees optimal ans
                r = middle - 1;
            } else {
                l = middle + 1;
            }

        }
        return ans;
    }
};
