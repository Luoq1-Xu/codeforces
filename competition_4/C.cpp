#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int testcases;
    cin >> testcases;
    
    while (testcases--) {
        int n, k;
        cin >> n >> k;
        
        vector<int> s(n), t(n);
        for (int i = 0; i < n; i++) {
            cin >> s[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> t[i];
        }
        
        unordered_map<int, int> s_mods;
        for (int e : s) {
            s_mods[e % k]++;
        }
        
        bool possible = true;
        for (int e : t) {
            int mod_class = e % k;
            int alt = (k - mod_class) % k;
            
            if (s_mods[mod_class] > 0) {
                s_mods[mod_class]--;
            } else if (s_mods[alt] > 0) {
                s_mods[alt]--;
            } else {
                possible = false;
                break;
            }
        }
        
        if (possible) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
    
    return 0;
}