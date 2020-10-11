#include <bits/stdc++.h> 
using namespace std; 
  
struct Node 
{ 
    int data; 
    struct Node* left, *right; 
}; 
  
bool isBST(Node* root, Node* l=NULL, Node* r=NULL) 
{ 
    if (root == NULL) 
        return true; 
    if (l != NULL and root->data <= l->data) 
        return false; 
    if (r != NULL and root->data >= r->data) 
        return false; 
  
    return isBST(root->left, l, root) and isBST(root->right, root, r); 
} 
  
struct Node* newNode(int data) 
{ 
    struct Node* node = new Node; 
    node->data = data; 
    node->left = node->right = NULL; 
    return (node); 
} 
  
int main() 
{ 
    struct Node *root = newNode(3); 
    root->left        = newNode(2); 
    root->right       = newNode(5); 
    root->left->left  = newNode(1); 
    root->left->right = newNode(4); 
  
    if (isBST(root,NULL,NULL)) 
        cout << "Given binary tree is a Binary Search Tree"; 
    else
        cout << "Given binary tree is not a Binary Search Tree"; 
  
    return 0; 
} 