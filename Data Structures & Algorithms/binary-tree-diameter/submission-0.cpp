/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int res = 0;
        dfs(root, res);
        return res;
    }
private:
    int dfs(TreeNode* root, int& res) {
        if (!root) {
            return 0;
        }
        int right = dfs(root->right, res);
        int left = dfs(root->left, res);

        res = max(res, right+left); //update res if right plus left is greater
        return 1 + max(right, left); //return the max when you go higher up
         // To the parent, this subtree is worth its deeper side, plus the edge
        // connecting to the parent. Can't return left+right: a path through
        // the parent may only pass through one of our two branches.
    }
};
