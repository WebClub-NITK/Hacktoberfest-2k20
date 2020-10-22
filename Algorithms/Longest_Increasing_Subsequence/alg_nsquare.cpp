#include <bits/stdc++.h>
using namespace std;

vector<int> longestIncreasingSubsequence(vector<int> inputVector)
{
    int n = inputVector.size();
    int *dp = new int[n+1], *pre = new int[n+1];
    fill(dp, dp + n+1, 0);
    fill(pre, pre + n+1, -1);
    dp[0] = 1;
    for(int i = 1; i < n; i++)
    {
        for(int j = 0; j < i; j++)
        {
            if(inputVector[i] > inputVector[j] && dp[i] < dp[j]+1)
            {
                dp[i] = dp[j] + 1;
                pre[i] = j;
            }
        }
    }
    vector <int> ret;
    int now = 0;
    for(int i = 0; i < n; i++)
    {
        if(dp[now] < dp[i]) now = i;
    }
    while(now != -1)
    {
        ret.push_back(inputVector[now]);
        now = pre[now];
    }
    reverse(ret.begin(), ret.end());
    return ret;
}

int main()
{
    int n;
    cin >> n;
    vector <int> v;
    v.resize(n);
    for(int i = 0; i < n; i++) cin >> v[i];
    vector <int> lis = longestIncreasingSubsequence(v);
    for(auto i: lis) cout << i << ' ';
    cout << endl;
    return 0;
}