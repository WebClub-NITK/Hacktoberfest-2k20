#include <bits/stdc++.h>
#define BIT_SIZE 32
using namespace std;

struct Trie
{
    int num;
    Trie *nxt[2];

    Trie()
    {
        num = 0;
        nxt[0] = nxt[1] = nullptr;
    }
    ~Trie()
    {
        if(nxt[0]) delete nxt[0];
        if(nxt[1]) delete nxt[1];
    }
    void insert(int val, int i)
    {
        if(i == -1)
        {
            num = val;
            return;
        }
        int bit = (val >> i) & 1;
        if(nxt[bit] == nullptr)
        {
            nxt[bit] = new Trie();
        }
        nxt[bit]->insert(val, i-1);
    }
    int query(int val, int i)
    {
        if(i == -1) return val^num;
        int bit = (val >> i) & 1;
        if(nxt[1-bit] != nullptr)
        {
            return nxt[1-bit]->query(val, i-1);
        }
        else
        {
            return nxt[bit]->query(val, i-1);
        }
    }
};

int findMaximumXor(int n, int arr[])
{
    Trie *root = new Trie();
    root->insert(0, BIT_SIZE-1);

    int ret = INT_MIN, xor_val = 0;
    for(int i = 0; i < n; i++)
    {
        xor_val = xor_val ^ arr[i];
        root->insert(xor_val, BIT_SIZE-1);
        ret = max(ret, root->query(xor_val, BIT_SIZE-1));
    }
    return ret;
}

int main()
{
    int n;
    cin >> n;
    int *arr = new int[n];

    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "Maximum Subarray Xor: " << findMaximumXor(n, arr);

    delete[] arr;
    return 0;
}