//Time complexity -O(n)

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
    int helper(TreeNode* root, int & res){
        if(root==NULL)
            return 0;
        
        if(root->left==NULL and root->right==NULL)
            return 1;
        int l=helper(root->left, res);      // max height of left subtree
        int r=helper(root->right, res);     // max height of right subtree

        res= max(res, 1+l+r);              
        return 1+max(l,r);
        
        
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int res=1;   //it will store the final diameter
        int ans=helper(root,res);
        return res-1;   
        //if edges reperesents the length of path between two nodes(as in case of leetcode question) return res-1
        // else if we count vertices the return res.
    }
};
