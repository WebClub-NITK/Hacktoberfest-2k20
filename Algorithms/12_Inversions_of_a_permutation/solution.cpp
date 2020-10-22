#include <vector>
#include <algorithm>

using namespace std;

vector<int> findInversions(int n, vector<int> p) {
    vector<int> tree(n + 1), res(n), v(n + 1);

    for (int i = 1; i <= n; i++) {
        v[p[i - 1]] = i;
    }

    for (int i = n; i > 0; i--) {
        for (int j = v[i]; j > 0; j -= j & -j) res[i - 1] += tree[j];
        for (int j = v[i]; j <= n; j += j & -j) tree[j]++;
    }

    return res;
}