#include <bits/stdc++.h>
using namespace std;

/*
Time complexity of Fibonacci Search: O(LogN)
Uses divide and conquer
*/

int FibonacciSearch(vector<int> &arr, int target)
{
  // finding the length of the array
  int n = arr.size();

  /*
    Consider m = 2
    ele2 contains the m-2th fibonacci number
    ele2 contains the m-1th fibonacci number
    ele contains the mth fibonacci number
  */
  int ele2 = 0;
  int ele1 = 1;
  int ele = ele1 + ele2;

  // setting ele to the smallest fibonacci number greater than or equal to n
  while (ele < n)
  {
    ele2 = ele1;
    ele1 = ele;
    ele = ele1 + ele2;
  }

  // marks the eliminated range from the front
  int offset = -1;

  while (ele > 1)
  {
    int i = min(offset + ele2, n - 1);

    // if target value is greater than the value at index i
    // cut the sbubarray from offset to i
    if (arr[i] < target)
    {
      ele = ele1;
      ele1 = ele2;
      ele2 = ele - ele1;
      offset = i;
    }

    // if the target value is less than the value at index i
    // cut the subarray from i+1 to n-1
    else if (arr[i] > target)
    {
      ele = ele2;
      ele1 = ele1 - ele2;
      ele2 = ele - ele1;
    }

    // element found return index
    else
      return i;
  }

  // checking the last element of the array if it matches with the target value
  if (ele1 > 0 and arr[offset + 1] == target)
  {
    return offset + 1;
  }

  // element not found
  return -1;
}

/* Driver function */
int main()
{
  int n;
  vector<int> arr;
  cout << "\nEnter the number of elements of the array: ";
  cin >> n;
  arr.resize(n);
  cout << "\nEnter the elements of the array respectively: \n";
  for (int i = 0; i < n; i++)
  {
    cin >> arr[i];
  }
  int target;
  cout << "\nEnter the element you want to search: ";
  cin >> target;
  int res = FibonacciSearch(arr, target);
  if (res == -1)
  {
    cout << "\nElement not found in the array!\n";
  }
  else
  {
    cout << "\nElement found at index: " << res << '\n';
  }
  return 0;
}