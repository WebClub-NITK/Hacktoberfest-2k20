// C++ implementation to find longest increasing subsequence in O(n Log n) time.
#include <bits/stdc++.h>
using namespace std;

// Binary search
int GetCeilIndex(vector<int> arr, vector<int>& T, int l, int r,int key)
{
	while (r - l > 1) {
		int m = l + (r - l) / 2;
		if (arr[T[m]] >= key)
			r = m;
		else
			l = m;
	}

	return r;
}

vector<int> LongestIncreasingSubsequence(vector<int>arr, int n)
{
	
	vector<int> tailIndices(n, 0); // Initialized with 0
	vector<int> prevIndices(n, -1); // initialized with -1
	vector<int>lis;

	int len = 1; // it will always point to empty location
	for (int i = 1; i < n; i++) {
		if (arr[i] < arr[tailIndices[0]]) {
			// new smallest value
			tailIndices[0] = i;
		}
		else if (arr[i] > arr[tailIndices[len - 1]]) {
			// arr[i] wants to extend largest subsequence
			prevIndices[i] = tailIndices[len - 1];
			tailIndices[len++] = i;
		}
		else {
			/* arr[i] wants to be a potential candidate of future subsequence
		       It will replace ceil value in tailIndices*/
			int pos = GetCeilIndex(arr, tailIndices, -1,
								len - 1, arr[i]);

			prevIndices[i] = tailIndices[pos - 1];
			tailIndices[pos] = i;
		}
	}

	for (int i = tailIndices[len - 1]; i >= 0; i = prevIndices[i])
        lis.push_back(arr[i]);
    reverse(lis.begin(),lis.end());


	return lis;
}

int main()
{
	int n;
	cout<<"Enter size of list"<<endl;
	cin>>n;
	vector<int>arr(n);
	cout<<"Enter the sequence"<<endl;
	for(int i=0;i<n;i++)
        cin>>arr[i];

	vector<int> lis= LongestIncreasingSubsequence(arr, n);
	cout<<"Longest Increasing Sequence is :  ";
    for(auto i=lis.begin();i!=lis.end();++i)
        cout<<*i<<" ";
    cout<<endl;
	return 0;
}
