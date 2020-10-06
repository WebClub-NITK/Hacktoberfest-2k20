#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int a[3], b[3];

    for (int i = 0; i < 3; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < 3; i++) {
        cin >> b[i];
    }

    int ma = 0;
    ma += min(a[0], b[1]);
    ma += min(a[1], b[2]);
    ma += min(a[2], b[0]);
    cout << ma << " ";

    int mi = 0;
    mi += max(a[0] - n + b[1], 0);
    mi += max(a[1] - n + b[2], 0);
    mi += max(a[2] - n + b[0], 0);
    cout << mi << " ";
}