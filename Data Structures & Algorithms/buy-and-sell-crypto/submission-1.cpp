class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxprofit = 0; 
        int l = 0; 
        int r = 1;
        while (r < prices.size()) {
            if (prices[l] > prices[r]) l = r;
            else maxprofit = max(maxprofit, prices[r] - prices[l]);
            r++;

        }
        return maxprofit;
    }
};
