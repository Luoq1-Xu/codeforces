#include <iostream>

using namespace std;
int main() {
    int size;
    cin >> size;

    if (size % 2 != 0) {
        cout << -1 << endl;
    } else {
        for (int i = 2; i < size + 1; i+=2) {
            cout << i << " " << i - 1 << " ";
        }
        cout << endl;
    }
    return 0;
}