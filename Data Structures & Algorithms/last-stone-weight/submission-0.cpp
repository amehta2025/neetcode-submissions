#include <queue>
using namespace std;
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap;
        for (int i : stones) {
            maxHeap.push(i);
        }
        while (maxHeap.size() > 1) {
            int first = maxHeap.top();
            maxHeap.pop();
            int second = maxHeap.top();
            maxHeap.pop();
            if (second < first) {
                maxHeap.push(first - second);
            }
        }

        return (maxHeap.size() == 0) ? 0 : maxHeap.top();
    }
};
